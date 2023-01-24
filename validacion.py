import csv, subprocess, os

from modelo import MX_Persistent_Customer_ID_VOD_viewership_Daily

max_lines = 100000

def validate_reports(directories_to_validate):
    
    print(
        "-------------------- VALIDATION STARTED -----------------------"
    )

    for dict_directory in directories_to_validate:
        directory = dict_directory['path']
        print(f'THE DIRECTORY IS {directory}')
        files = os.listdir(directory)
        print(f"THE FILES ARE {files}")
        chunks = []
        
        for file in files:
            chunks.append(file) if file.startswith("chunk") else None
        
        for chunk in chunks:
            print(f"READING THE CHUNK {directory}/{chunk}")
            print(f"WRITING THE CHUNK {directory}/transformed_{chunk}")
            
            with open(f"{directory}/{chunk}", "r", newline="") as raw_csv, \
                    open(f"{directory}/transformed_{chunk}", "w", newline="") as transformed_csv:
                new_header = list()
                r = csv.reader(raw_csv)
                w = csv.writer(transformed_csv)
                header = r.__next__()
                for head in header:
                    new_header.append(head.replace('"', '').replace(" ", "_").replace("/", "_"))
                w.writerow(new_header)
                for row in r:
                    w.writerow(row)
                    
            print(f"READING THE CHUNK {directory}/transformed_{chunk}")
            print(f"WRITING THE CHUNK {directory}/validated_{chunk}")
            
            with open(f"{directory}/transformed_{chunk}", "r", newline="") as transformed_csv, \
                    open(f"{directory}/validated_{chunk}", "w", newline="") as validated_csv:
                csv_reader = csv.DictReader(transformed_csv)
                headers = csv_reader.fieldnames
                csv_reader = list(csv_reader)

                new_model = map(MX_Persistent_Customer_ID_VOD_viewership_Daily.parse_obj, csv_reader)
                new_model = list(map(lambda user: user.dict(), new_model))

                dict_writer = csv.DictWriter(validated_csv, headers)
                dict_writer.writeheader()
                dict_writer.writerows(new_model)


def split_data():
    files = os.listdir('./unprocessed_reports')
    print("THE PROCESS WILL SPLIT THE FOLLOWING FILES: " + str(files))
    chunks_list = list()
    for raw_file in files:
        # raw_file_path = "./unprocessed_reports/" + str(raw_file)
        raw_file_path = f"./unprocessed_reports/{raw_file}" 
        num_raw_lines = int(subprocess.getoutput("wc -l " + str(raw_file_path)).split(" ")[0]) - 1
        chunks_path = "./splitted_reports/chunks_" + str(raw_file)
        print("RAW FILE PATH: " + str(raw_file_path))
        print("THE RAW FILE " + str({raw_file}) + " HAS " + str(num_raw_lines) + " LINES")
        print("CHUNKS PATH: " + str(chunks_path))
        os.makedirs(chunks_path, exist_ok=True)
        
        with open(raw_file_path, "r") as raw_csv, \
                open(str(chunks_path)+"/header.csv", "w") as headers:
            r = csv.reader(raw_csv)
            header = next(r)
            header.append("SourceFile")
            w = csv.writer(headers)
            w.writerow(header)
        
        subprocess.getoutput(
            "tail -n +2 " + str(raw_file_path) + " >> " + str(chunks_path) + "/no_header.csv"
        )
        subprocess.getoutput(
            "split -l " + str(max_lines) + " -d " + str(chunks_path) + "/no_header.csv " + str(chunks_path) +"/chunk_tmp_  -a 5"
        )
        subprocess.getoutput("rm -f " + str(chunks_path) + "/_no_header.csv")
        num_of_chunks = int(
            subprocess.getoutput("ls " + str(chunks_path) + "/chunk_tmp_* | wc -l")
        )
        if not num_of_chunks:
            print("THE RAW FILE " + str(raw_file) + " DOES NOT HAVE ANY CHUNK")
            continue
        print("THE RAW FILE " + str(raw_file) + " HAS " + str(num_of_chunks) + " CHUNKS")
        
        for chunk in range(num_of_chunks):
            chunk = "{:05d}".format(chunk)
            chunk_tmp_file = str(chunks_path) + "/chunk_tmp_" + str(chunk)
            subprocess.getoutput(
                "cat " + str(chunks_path) + "/header.csv " + str(chunk_tmp_file) + " >> " + str(chunks_path) + "/chunk_" + str(chunk) + ".csv"
            )
            subprocess.getoutput("rm -rf " + str(chunk_tmp_file))
        
        chunks_list.append(
            {
                "path": chunks_path,
                "num_files": num_of_chunks,
                "raw_file_date": raw_file.split(".")[0],
            }
        )
        print()
    print(chunks_list)
    return chunks_list

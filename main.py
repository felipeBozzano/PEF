import validacion

def main():
    splitted_data = validacion.split_data()
    validacion.validate_reports(splitted_data)

if __name__ == "__main__":
    main()
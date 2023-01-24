from datetime import datetime

from pydantic import BaseModel, Field, validator


def int_to_str(v):
    if not v:
        return None
    try:
        v = str(v)
    except:
        v = None
    return v


def date_format(v):
    try:
        validation = datetime.strptime(v, "%Y-%m-%d").date()
    except:
        validation = None
    v = v if validation else None
    return v


def change_empty_by_null(v):
    if not v:
        v = None
    return v


def username_alphanumeric(v):
    valid_formats = [
        "%Y-%m-%d",
        "%Y-%m-%d %H:%M",
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%d %H:%M:%S%z",
        "%Y-%m-%d %H:%M:%S%Z",
        "%Y-%m-%d %H:%M:%SZ",
        "%Y-%m-%d %H:%M:%S.%f",
        "%Y-%m-%d %H:%M:%S.%f%z",
        "%Y-%m-%d %H:%M:%S.%f%Z",
        "%Y-%m-%d %H:%M:%S.%fZ",
        "%Y-%m-%dT%H:%M",
        "%Y-%m-%dT%H:%M:%S",
        "%Y-%m-%dT%H:%M:%S%z",
        "%Y-%m-%dT%H:%M:%S%Z",
        "%Y-%m-%dT%H:%M:%SZ",
        "%Y-%m-%dT%H:%M:%S.%f",
        "%Y-%m-%dT%H:%M:%S.%f%z",
        "%Y-%m-%dT%H:%M:%S.%f%Z",
        "%Y-%m-%dT%H:%M:%S.%fZ",
        "%Y/%m/%d",
        "%Y/%m/%d %H:%M",
        "%Y/%m/%d %H:%M:%S",
        "%Y/%m/%d %H:%M:%S%z",
        "%Y/%m/%d %H:%M:%S%Z",
        "%Y/%m/%d %H:%M:%SZ",
        "%Y/%m/%d %H:%M:%S.%f",
        "%Y/%m/%d %H:%M:%S.%f%z",
        "%Y/%m/%d %H:%M:%S.%f%Z",
        "%Y/%m/%d %H:%M:%S.%fZ",
        "%Y/%m/%dT%H:%M",
        "%Y/%m/%dT%H:%M:%S",
        "%Y/%m/%dT%H:%M:%S%z",
        "%Y/%m/%dT%H:%M:%S%Z",
        "%Y/%m/%dT%H:%M:%SZ",
        "%Y/%m/%dT%H:%M:%S.%f",
        "%Y/%m/%dT%H:%M:%S.%f%z",
        "%Y/%m/%dT%H:%M:%S.%f%Z",
        "%Y/%m/%dT%H:%M:%S.%fZ",
    ]
    validation = 0
    for t_format in valid_formats:
        try:
            datetime.strptime(v, t_format)
            validation += 1
        except:
            pass
    v = v if validation else None
    return v


def is_int(v):
    try:
        v = int(v)
    except:
        v = None
    return v


def is_float(v):
    try:
        v = float(v)
    except:
        v = None
    return v


MX_PERSISTENT_CUSTOMER_ID_VOD_VIEWERSHIP_DAILY_SCHEMA = [
    {"name": "Report_Date", "type": "DATE", "mode": "NULLABLE"},
    {"name": "Marketplace_ID", "type": "INTEGER", "mode": "NULLABLE"},
    {"name": "Marketplace_Description", "type": "STRING", "mode": "NULLABLE"},
    {"name": "Offer_ID", "type": "STRING", "mode": "NULLABLE"},
    {"name": "Offer_Name", "type": "STRING", "mode": "NULLABLE"},
    {"name": "Encrypted_Customer_ID", "type": "STRING", "mode": "NULLABLE"},
    {
        "name": "Stream_Start_Timestamp",
        "type": "TIMESTAMP",
        "mode": "NULLABLE",
    },
    {"name": "Connection_Type", "type": "STRING", "mode": "NULLABLE"},
    {"name": "Stream_Type", "type": "STRING", "mode": "NULLABLE"},
    {"name": "Device_Class", "type": "STRING", "mode": "NULLABLE"},
    {"name": "Device_Subclass", "type": "STRING", "mode": "NULLABLE"},
    {"name": "State_Geography", "type": "STRING", "mode": "NULLABLE"},
    {"name": "Postal_Code", "type": "STRING", "mode": "NULLABLE"},
    {"name": "Playback_Method", "type": "STRING", "mode": "NULLABLE"},
    {"name": "Seconds_Viewed", "type": "FLOAT", "mode": "NULLABLE"},
    {"name": "Content_Type", "type": "STRING", "mode": "NULLABLE"},
    {"name": "Title_Name", "type": "STRING", "mode": "NULLABLE"},
    {"name": "Season_Number", "type": "INTEGER", "mode": "NULLABLE"},
    {"name": "Episode_Number", "type": "INTEGER", "mode": "NULLABLE"},
    {"name": "Studio_Name", "type": "STRING", "mode": "NULLABLE"},
    {"name": "Runtime_Minutes", "type": "INTEGER", "mode": "NULLABLE"},
    {"name": "Live_Linear_Channel_Name", "type": "STRING", "mode": "NULLABLE"},
    {"name": "Vendor_SKU", "type": "STRING", "mode": "NULLABLE"},
]

class MX_Persistent_Customer_ID_VOD_viewership_Daily(BaseModel):
    Report_Date: str = Field(default=None)
    Marketplace_ID: int = Field(default=None)
    Marketplace_Description: str = Field(default=None)
    Offer_ID: str = Field(default=None)
    Offer_Name: str = Field(default=None)
    Encrypted_Customer_ID: str = Field(default=None)
    Stream_Start_Timestamp: str = Field(default=None)
    Connection_Type: str = Field(default=None)
    Stream_Type: str = Field(default=None)
    Device_Class: str = Field(default=None)
    Device_Subclass: str = Field(default=None)
    State_Geography: str = Field(default=None)
    Postal_Code: str = Field(default=None)
    Playback_Method: str = Field(default=None)
    Seconds_Viewed: float = Field(default=None)
    Content_Type: str = Field(default=None)
    Title_Name: str = Field(default=None)
    Season_Number: int = Field(default=None)
    Episode_Number: int = Field(default=None)
    Studio_Name: str = Field(default=None)
    Runtime_Minutes: int = Field(default=None)
    Live_Linear_Channel_Name: str = Field(default=None)
    Vendor_SKU: str = Field(default=None)

    _normalize_postal_code = validator(
        "Postal_Code", pre=True, always=True, allow_reuse=True
    )(int_to_str)
    _normalize_report_date = validator("Report_Date", allow_reuse=True)(
        date_format
    )
    _change_empty_by_null = validator(
        "Marketplace_Description",
        "Offer_ID",
        "Offer_Name",
        "Encrypted_Customer_ID",
        "Connection_Type",
        "Stream_Type",
        "Device_Class",
        "Device_Subclass",
        "State_Geography",
        "Playback_Method",
        "Content_Type",
        "Title_Name",
        "Studio_Name",
        "Live_Linear_Channel_Name",
        "Vendor_SKU",
        allow_reuse=True,
    )(change_empty_by_null)
    _username_alphanumeric = validator(
        "Stream_Start_Timestamp", allow_reuse=True
    )(username_alphanumeric)
    _is_int = validator(
        "Marketplace_ID",
        "Season_Number",
        "Episode_Number",
        "Runtime_Minutes",
        allow_reuse=True,
        pre=True,
        always=True,
    )(is_int)
    _is_float = validator(
        "Seconds_Viewed", allow_reuse=True, pre=True, always=True
    )(is_float)

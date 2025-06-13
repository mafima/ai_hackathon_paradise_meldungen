import socket
import time
import os


# put all data unzipped in the data folder


link = "https://shorturl.at/hcHtb"
path = "/home/manu/DEV/AI/ai_hackathon_paradise_meldungen/data"
path_add = "/maengel/maengel"
path_final = path + path_add # This is the correct way to append


# JSON Format Example:
data_json = {
    "title": "#123",
    "service_request_id": "3",
    "description": "<p> text </p>\n",
    "media_url": "",
    "service_name": "Straße, ",
    "service_code": "12_straße",
    "processing_status": "Geschlossen",
    "geolocation_latitude": "12.3",
    "geolocation_longitude": "11.1",
    "requested_datetime": "<time datetime=\"2018</time>\n",
    "updated_datetime": "<time datetime=\"2021</time>\n"
}

def run_client():
    print("Client start.")
    # count all json containing html tag.
    filter_string = "<hlink="
    count = sum(1 for file in os.listdir(path_final) if filter_string in file)
    print(f"Number of JSON files with '{'<hlink=':', count}")
    print("Client closed.")

if __name__ == "__main__":
    run_client()
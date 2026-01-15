import os
import csv

def read_csv_config(file_path, setting_title, value_title):
    if not os.path.isfile(file_path):
       raise FileNotFoundError(f"File not found: {file_path}")

    config_dict = {}
    
    with open(file_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
    
        for row in reader:
            function_name = row[setting_title].strip()
            pin_raw = row[value_title].strip()
        
            try:
                # Attempt to convert to integer
                pin_value = int(pin_raw)
            except ValueError:
                # Fallback to string if it's not an integer
                pin_value = pin_raw
            config_dict[function_name] = pin_value
    return config_dict
    
def read_csv_setting(file_path, setting_name, setting_value):
    return {}
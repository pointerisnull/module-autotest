import os
import csv

# Read all settings from a CSV file
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
                # Ensure integers are returned as such
                pin_value = int(pin_raw)
            except ValueError:
                # Fallback to string if it's not an integer
                pin_value = pin_raw
            config_dict[function_name] = pin_value
    return config_dict
    
# Read a single setting from a CSV file
def read_csv_setting(file_path, setting_name):
    try:
        with open(file_path, mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)
           
            for row in reader:
                if row[0].strip() == setting_name:
                    raw_value = row[1].strip()
                    
                    # Ensure integers are returned as such
                    try:
                        return int(raw_value)
                    except ValueError:
                        return raw_value 
    except FileNotFoundError:
        return f"Error: File '{file_path}' not found."
    
    return None
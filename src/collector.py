import json
import pandas as pd
from typing import Literal
import re
from tqdm import tqdm
import os

DATA_ROOT = "./data"

class Collector:
    @staticmethod
    def collect_folder_names(dir, pattern):
        matches = []
        for folder in os.listdir(dir):
            folder_path = os.path.join(dir, folder)
            if os.path.isdir(folder_path) and re.match(pattern, folder):
                matches.append(folder_path)
        return matches
    
    @staticmethod
    def collect_data(years,
                     chamber=Literal["h","s"],
                     dir=DATA_ROOT
    ):
        pattern = chamber + r"\d+"
        folders = []
        for year in years:
            year_folders = Collector.collect_folder_names(os.path.join(dir, str(year)), pattern)
            print(f"Found {len(year_folders)} for the year {year}")
            folders.extend(year_folders)
            
        print(f"Found in total {len(folders)} entries")
            
        data_list = []
        for folder in tqdm(folders):
            json_path = os.path.join(folder, "data.json")
            try:
                f = open(json_path, "r")
                json_data = json.load(f)
                data_list.append(json_data)
            except:
                print(f"Error reading {json_path}")
        return data_list
    

        
            
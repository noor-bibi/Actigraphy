

import os
import pandas as pd
import numpy as np


def list_files_recursive(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            print(file_path)
            print(root)
            print(file)justthecodenotfiles so just Run_All_mice.py?yes got it Zoom might end. noCreate a zoom session if iendtedh inkithinkwearegood.wejustneedtopateitandthatsit ok let me showyou a fast way 


            df = pd.read_csv(file_path, engine='python', encoding='latin1', skiprows=7)
            total = df.sum(axis=0)
            print(total)

def cri(sleep_times, wake_times):
    sleep_times = sleep_times * 60
    wake_times = wake_times * 60
    delta_times = wake_times - sleep_times
    average_delta_time = np.mean(delta_times)
    cri = (average_delta_time - 60) / 60
    return cri
sleep_times = [7]
wake_times = [19]

cri = cri(sleep_times, wake_times)

print(cri)




# Example usage:
folder_path = ".\For_Noor\GL261P2L\GR_KD\Analysis_GR_KD"
list_files_recursive(folder_path)


# Specify the file path


# Load the CSV file into a DataFrame

# Now, 'df' contains your data as a DataFrame, and you can work with it as needed.


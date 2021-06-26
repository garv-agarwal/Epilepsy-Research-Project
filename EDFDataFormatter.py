import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision
import numpy as np
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
import tensorflow as tf
import pandas as pd
import os
import mne

database = os.listdir("E:\MIT-CHB EEG Data\chb-mit-scalp-eeg-database-1.0.0")
input_data = []
input_labels = []
# iterating through every folder in the database
for patient in database:
    # making sure only patient folders are used
    if patient.startswith("chb"):
        patient_folder = os.listdir("E:\MIT-CHB EEG Data\chb-mit-scalp-eeg-database-1.0.0\\" + patient)
        # one array per patient, each element being one EEG file
        patient_data = []
        patient_labels = []
        # iterating through files
        for file in patient_folder:
            if file.endswith(".edf"):
                full_file = "E:\MIT-CHB EEG Data\chb-mit-scalp-eeg-database-1.0.0\\" + patient + "\\" + file
                print(full_file)
                # reading the EDF (EEG) signal
                data = mne.io.read_raw_edf(full_file)
                raw_data = data.get_data()
                info = data.info
                channels = data.ch_names
                # turning the file into a data_frame and removing the time column
                data_frame = data.to_data_frame()
                del data_frame['time']
                patient_data.append(data_frame.values)
                # creating the labels for whether a file depicts a seizure or not
                if (file + ".seizures") in patient_folder:
                    patient_labels.append(1)
                else:
                    patient_labels.append(0)
        # appending the arrays to the list with the entire dataset
        input_data.append(patient_data)
        input_labels.append(patient_labels)


# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 11:25:11 2024

@author: ranui
"""

import pandas as pd
import os
from shutil import copyfile

def segregate_images(input_excel, image_folder, output_folder):
    # Read the Excel sheet into a DataFrame
    df = pd.read_excel(input_excel)

    # Create output folders if they don't exist
    os.makedirs(output_folder, exist_ok=True)

    # Iterate through the DataFrame and move images to respective folders
    for index, row in df.iterrows():
        image_name = row['imagePath']  # Replace 'ImageName' with the actual column name in your Excel sheet
        class_label = row['Healthy']  # Replace 'ClassLabel' with the actual column name in your Excel sheet

        # Create class-specific folder if it doesn't exist
        class_folder = os.path.join(output_folder, str(class_label))
        os.makedirs(class_folder, exist_ok=True)

        # Construct source and destination paths
        source_path = os.path.join(image_folder, image_name)
        destination_path = os.path.join(class_folder, image_name)

        # Copy the image to the respective class folder
        copyfile(source_path, destination_path)

# Example usage
input_excel = 'D:/data_split_excelsheet/PCOSGen-train/PCOSGen-train/class_label_r.xlsx'
image_folder = 'D:/data_split_excelsheet/PCOSGen-train/PCOSGen-train/images'
output_folder = 'D:/data_split_excelsheet/PCOSGen-train/output'

segregate_images(input_excel, image_folder, output_folder)
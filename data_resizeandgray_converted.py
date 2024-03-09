# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 11:54:03 2024

@author: ranui
"""

import cv2
import os

# # Specify the input and output folders
input_folder = "D:/data_split_excelsheet/PCOS_test/images"
output_folder = "D:\data_split_excelsheet\PCOS_test\converted_gray"

# # Create the output folder if it doesn't exist
# if not os.path.exists(output_folder):
#     os.makedirs(output_folder)

# # List all files in the input folder
files = os.listdir(input_folder)

for file in files:
#     # Construct the full path for the input file
     input_path = os.path.join(input_folder, file)

#     # Read the image using cv2
     original_image = cv2.imread(input_path)

#     # Resize the image to 128x128 pixels
     resized_image = cv2.resize(original_image, (128, 128))

#     # Convert the image to grayscale
     grayscale_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

#     # Construct the full path for the output file
     output_path = os.path.join(output_folder, file)

#     # Save the processed image to the output folder
     cv2.imwrite(output_path, grayscale_image)

print("Images processed and saved to the output folder.")
# here we have take converted image and check size and shape
img = cv2.imread(r"D:/data_split_excelsheet/PCOS_test/converted_gray/image10002.jpg")
cv2.imshow(img)
print(img.shape)
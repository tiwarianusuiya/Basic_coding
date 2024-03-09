# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 22:00:53 2024

@author: ranui
"""

import cv2
import matplotlib.pyplot as plt

# Load an image using cv2.imread()
image_path = 'path_to_your_image.jpg'
image = cv2.imread(image_path)

# Check if the image is successfully loaded
if image is not None:
    # Display the image using matplotlib
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.show()

    # Print the shape of the image
    print("Image Shape:", image.shape)
else:
    print("Error loading the image.")

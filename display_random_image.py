# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 19:30:42 2021

@author: asarkar
"""

import random
import matplotlib.pyplot as plt

def display_image(dataset):
# Adjust the size of your images
    plt.figure(figsize=(20,10))

    for i in range(9):
        num = random.randint(0,len(dataset)-1)
        plt.subplot(3, 3, i + 1)
    
        plt.imshow(dataset[num])
        plt.axis('off')
    
# Adjust subplot parameters to give specified padding
    plt.tight_layout()

# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 19:36:34 2021

@author: asarkar
"""

import matplotlib.pyplot as plt

def display_bar_chart(data_labels):
    
    labels = ['Level_0','Level_1','Level_2','Level_3','Level_4']

    level_0 = 0
    level_1 = 0
    level_2 = 0
    level_3 = 0
    level_4 = 0

    for i in data_labels:
        
        if i==0:
            level_0 += 1
        elif i==1:
            level_1 += 1
        elif i==2:
            level_2 += 1
        elif i ==3:
            level_3 += 1
        else:
            level_4 += 1
            
    print('Number of Level_0 images = ',level_0)
    print('Number of Level_1 images = ',level_1)
    print('Number of Level_2 images = ',level_2)
    print('Number of Level_3 images = ',level_3)
    print('Number of Level_4 images = ',level_4)
    
    # plotting the data

    xe = [i for i, _ in enumerate(labels)]

    numbers = [level_0,level_1,level_2,level_3,level_4]
    colors = ['green','blue','black','yellow','red']
    plt.bar(xe,numbers,color = colors)
    plt.xlabel("Labels")
    plt.ylabel("No. of images")
    plt.title("Images for each label")

    plt.xticks(xe, labels)

    plt.show()

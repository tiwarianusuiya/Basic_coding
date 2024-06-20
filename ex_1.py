# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 11:34:12 2024

@author: nayek
"""
# linear regression
import math
def sigmoid(x):
    return 1 / (1+math.exp(-x))
sigmoid(1)

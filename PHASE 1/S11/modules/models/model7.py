# -*- coding: utf-8 -*-
"""model7.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Z75hDrqLEaCWYzHUPgqLG9USrfvv94Hg
"""

from __future__ import print_function
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
# %matplotlib inline
import matplotlib.pyplot as plt
import torchvision
import numpy as np


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        dropout_value=0.1


        self.conv1 = nn.Sequential(nn.Conv2d(in_channels=3, out_channels=32, kernel_size=3, padding=1),
                                   nn.ReLU(),
                                   nn.BatchNorm2d(32),
                                   nn.Dropout(dropout_value))
            
                                                                                   # Input: 32x32x3 | Output: 32x32x32 | RF: 3x3



        self.conv2 = nn.Sequential(nn.Conv2d(in_channels=32, out_channels=32, kernel_size=3, padding=1),
                                   nn.ReLU(),
                                   nn.BatchNorm2d(32),
                                   nn.Dropout(dropout_value))
           
                                                                                   # Input: 32x32x32 | Output: 32x32x32 | RF: 5x5



        self.conv3 = nn.Sequential(nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, padding=2, dilation=2),
                                   nn.ReLU(),
                                   nn.BatchNorm2d(64),
                                   nn.Dropout(dropout_value))
        
                                                                                   # Input: 32x32x32 | Output: 32x32x32 | RF: 9x9



        self.pool1 = nn.MaxPool2d(2, 2)                                            # Input: 32x32x32 | Output: 16x16x32 | RF: 10x10


        self.conv4 = nn.Sequential(nn.Conv2d(in_channels=64, out_channels=64, kernel_size=3, padding=2, dilation=2),
                                   nn.ReLU(),
                                   nn.BatchNorm2d(64),
                                   nn.Dropout(dropout_value) )
          
           
                                                                                   # Input: 16x16x32 | Output: 16x16x64 | RF: 18x18



        self.conv5 = nn.Sequential(nn.Conv2d(in_channels=64, out_channels=64, kernel_size=3, padding=2, dilation=2),
                                   nn.ReLU(),
                                   nn.BatchNorm2d(64),
                                   nn.Dropout(dropout_value)) 
            
            
                                                                                   # Input: 16x16x64 | Output: 16x16x64 | RF: 26x26


        #depthwise convolution
        self.conv6 = nn.Sequential(nn.Conv2d(in_channels=64, out_channels=128,kernel_size=3,padding=1,groups=64),
                                   nn.Conv2d(in_channels=128,out_channels=128,kernel_size=1),
                                   nn.ReLU(),
                                   nn.BatchNorm2d(128),
                                   nn.Dropout(dropout_value))
                                                                                   # Input: 16x16x64 | Output: 16x16x64 | RF: 30x30



        self.pool2 = nn.MaxPool2d(2, 2)                                            # Input: 16x16x64 | Output: 8x8x64 | RF: 32x32

        #depthwise convolution
        self.conv7 = nn.Sequential( nn.Conv2d(in_channels=128, out_channels=128,kernel_size=3,padding=1,groups=128),           
                                    nn.Conv2d(in_channels=128,out_channels=128,kernel_size=1),
                                    nn.ReLU(),
                                    nn.BatchNorm2d(128),
                                    nn.Dropout(dropout_value))
                                                                                   # Input: 8x8x64 | Output: 8x8x128 | RF: 40x40

        # dilation
        self.conv8 = nn.Sequential(nn.Conv2d(in_channels=128, out_channels=128, kernel_size=3, padding=2, dilation=2),            
                                   nn.ReLU(),
                                   nn.BatchNorm2d(128),
                                   nn.Dropout(dropout_value))
                                                                                  # Input: 8x8x128 | Output: 8x8x128 | RF: 56x56


        self.pool3 = nn.MaxPool2d(2, 2)                                           # Input: 8x8x128 | Output: 4x4x128 | RF: 60x60


        self.gap =nn.AvgPool2d(kernel_size=4)
                                                                                  # Input: 4x4x128 | Output: 1x1x128 | RF: 84x84


        self.fc = nn.Linear(128, 10)                                              # Input: 1x1x128 | Output: 1x1x10 | RF: 84x84



    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        x = self.conv3(x)
        x = self.pool1(x)
        x = self.conv4(x)
        x = self.conv5(x)
        x = self.conv6(x)
        x = self.pool2(x)
        x = self.conv7(x)
        x = self.conv8(x)
        x = self.pool3(x)
        x = self.gap(x)
        x = x.view(-1, 128)
        x = self.fc(x)
        return x
# -*- coding: utf-8 -*-
"""train10.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DbATpevWgqyzYwfoTv-UQnGmw4RBQGR6
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
import torchvision.transforms as transforms
import albumentations
from albumentations.pytorch import ToTensor
from tqdm import tqdm

train_acc = []
train_losses = []
def train(model, device, train_loader, optimizer, loss_func, epoch):
  model.train()
  pbar = tqdm(train_loader)
  correct = 0
  processed = 0
  train_loss = 0
  for batch_idx, (data, target) in enumerate(pbar):
        # get the inputs
        data, target = data.to(device), target.to(device)

        # zero the parameter gradients
        optimizer.zero_grad()

        # predict
        y_pred = model(data)

        # loss
        loss = loss_func(y_pred, target)
        
        # backprop
        loss.backward()
        optimizer.step()

        # update pbar tqdm
        pred = y_pred.argmax(dim=1, keepdim=True)  # get the index of the max log-probability
        correct += pred.eq(target.view_as(pred)).sum().item()
        processed += len(data)
        train_loss += loss.item()

        pbar.set_description(desc= f'Epoch= {epoch} Loss={loss.item()} Batch_id={batch_idx} Accuracy={100*correct/processed:0.2f}')
  
  train_loss /= len(train_loader)
  train_losses.append(train_loss)
  train_acc.append(100*correct/processed)


# -*- coding: utf-8 -*-
"""train9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Co1-obLJbcyxnRMc-IfEylhxYOQ4r80W
"""

# Commented out IPython magic to ensure Python compatibility.
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

train_losses = []
train_acc = []
def train(model, device, train_loader, optimizer, loss_func, epoch):
  model.train()
  pbar = tqdm(train_loader)
  correct = 0
  processed = 0
  for batch_idx, (data, target) in enumerate(pbar):
        # get the inputs
        data, target = data.to(device), target.to(device)

        # zero the parameter gradients
        optimizer.zero_grad()

        # predict
        y_pred = model(data)

        # loss
        loss = loss_func(y_pred, target)
        train_losses.append(loss)
        # backprop
        loss.backward()
        optimizer.step()

        # update pbar tqdm
        pred = y_pred.argmax(dim=1, keepdim=True)  # get the index of the max log-probability
        correct += pred.eq(target.view_as(pred)).sum().item()
        processed += len(data)

        pbar.set_description(desc= f'Epoch= {epoch} Loss={loss.item()} Batch_id={batch_idx} Accuracy={100*correct/processed:0.2f}')
        train_acc.append(100*correct/processed)
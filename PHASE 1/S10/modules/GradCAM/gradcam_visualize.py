# -*- coding: utf-8 -*-
"""gradcam_visualize.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15Zo1QmUhembkF2u4aTRxTwPjmDy9n_4z
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
from tqdm import tqdm
import numpy as np
import torchvision.transforms as transforms
import albumentations
from albumentations.pytorch import ToTensor
import cv2
from .gradcam import GradCAM
from un_normalized import unnormalized

class GradCAMView(object):

	def __init__(self, model, classes, target_layers):
		super(GradCAMView, self).__init__()
		self.model = model
		self.classes = classes
		self.target_layers = target_layers
		self.device = next(model.parameters()).device

		self.gcam = GradCAM(model, target_layers, len(classes))
		
	def grad_cam(self, mask, img):
	    heatmap = (255 * mask.squeeze()).type(torch.uint8).cpu().numpy()
	    heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)
	    heatmap = torch.from_numpy(heatmap).permute(2, 0, 1).float().div(255)
	    b, g, r = heatmap.split(1)
	    heatmap = torch.cat([r, g, b])    
	    
	    result = heatmap+img.cpu()
	    result = result.div(result.max()).squeeze()
	    return heatmap, result

	def plot_heatmaps_indvidual(self, img_data, truth_class, pred_class, img_name):
		fig, axs = plt.subplots(nrows=2, ncols=5, figsize=(10, 4),
			subplot_kw={'xticks': [], 'yticks': []})
		fig.suptitle('GradCam for the class: \nActual: %s - Predicted: %s' % 
			( pred_class , truth_class ), fontsize=15, weight='medium', y=1.05)

		for ax, data in zip(axs.flat, img_data):
			img = data["img"]
			npimg = img.cpu().numpy()
			ax.imshow(np.transpose(npimg, (1, 2, 0)))
			ax.set_title("%s" % (data["label"]))

		plt.savefig(img_name)

	def plot_heatmaps(self, img_data, img_name):
		fig, axs = plt.subplots(nrows=len(img_data), ncols=3, figsize=(6, 50),
			subplot_kw={'xticks': [], 'yticks': []})

		for i in range(len(img_data)):
			data = img_data[i]
			for j in range(len(data)):
				img = data[j]["img"]
				npimg = img.cpu().numpy()
				axs[i][j].axis('off')
				axs[i][j].set_title(data[j]["label"])
				axs[i][j].imshow(np.transpose(npimg, (1, 2, 0)))

		fig.tight_layout()
		fig.savefig(img_name)


	def __call__(self, images, truth_image, target_layers, 
				metric="", per_image=True):
		masks_map, pred = self.gcam(images, target_layers   )
		if per_image:
			for i in range(len(images)):
				img = images[i]
				results_data = [{
					"img": unnormalized(img),
					"label": "Result:"
				}]
				heatmaps_data = [{
					"img": unnormalized(img),
					"label": "Heatmap:"
				}]
				for layer in target_layers:
					mask = masks_map[layer][i]
					heatmap, result = self.grad_cam(mask, unnormalized(img))
					results_data.append({
						"img": result,
						"label": layer
					})
					heatmaps_data.append({
						"img": heatmap,
						"label": layer
					})
				pred_class = self.classes[pred[i][0]]
				truth_class = self.classes[truth_image[i]]
				fname = "gradcam_%s_%s_t%s_p%s.png" % (metric, i, truth_class, pred_class)
				self.plot_heatmaps_indvidual(results_data+heatmaps_data, truth_class,
											pred_class, fname)
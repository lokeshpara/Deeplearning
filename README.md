# Assignment 11

### PrepLayer - Conv 3x3 s1, p1) >> BN >> RELU [64k]
### Layer1 -
### X = Conv 3x3 (s1, p1) >> MaxPool2D >> BN >> RELU [128k]
### R1 = ResBlock( (Conv-BN-ReLU-Conv-BN-ReLU))(X) [128k] 
### Add(X, R1)
### Layer 2 -
### Conv 3x3 [256k]
### MaxPooling2D
### BN
### ReLU
### Layer 3 -
### X = Conv 3x3 (s1, p1) >> MaxPool2D >> BN >> RELU [512k]
### R2 = ResBlock( (Conv-BN-ReLU-Conv-BN-ReLU))(X) [512k]
### Add(X, R2)
### MaxPooling with Kernel Size 4
### FC Layer 
### SoftMax


## Uses One Cycle Policy such that:
### Total Epochs = 24
### Max at Epoch = 5
### LRMIN = FIND
### LRMAX = FIND
### NO Annihilation
### Uses this transform -RandomCrop 32, 32 (after padding of 4) >> FlipLR >> Followed by CutOut(8, 8)
### Batch size = 512
### Target Accuracy: 90%. 

### Best test accuracy :92.22

Epoch: 23  LR:  0.004006000000000003
Epoch= 23 Loss=0.1974107176065445 Batch_id=97 Accuracy=93.89: 100%|██████████| 98/98 [00:23<00:00,  4.23it/s]
Test set: Average loss: 0.0004, Accuracy: 9222/10000 (92.22%)


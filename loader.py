{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "loader.py",
      "provenance": [],
      "collapsed_sections": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "accelerator": "GPU"
  },
  "cells": [
    {
      "cell_type": "code",
      "metadata": {
        "id": "ZLmTrjJO7qHt",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "from __future__ import print_function\n",
        "import torch\n",
        "import torch.nn as nn\n",
        "import torch.nn.functional as F\n",
        "import torch.optim as optim\n",
        "from torchvision import datasets, transforms\n",
        "%matplotlib inline\n",
        "import matplotlib.pyplot as plt\n",
        "import torchvision\n",
        "import numpy as np"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "WeNw40PAmxEZ",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "\n",
        "   \n",
        "\n",
        "transform = transforms.Compose(\n",
        "    [transforms.ToTensor(),\n",
        "     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])\n",
        "\n",
        "trainset = torchvision.datasets.CIFAR10(root='./data', train=True, download=True, transform=transform)\n",
        "testset = torchvision.datasets.CIFAR10(root='./data', train=False, download=True, transform=transform)  \n",
        "  \n",
        "SEED = 1\n",
        "\n",
        "# CUDA?\n",
        "cuda = torch.cuda.is_available()\n",
        "print(\"CUDA Available?\", cuda)\n",
        "\n",
        "# For reproducibility\n",
        "torch.manual_seed(SEED)\n",
        "\n",
        "if cuda:\n",
        "    torch.cuda.manual_seed(SEED)\n",
        "\n",
        "dataloader_args = dict(shuffle=True, batch_size=128, num_workers=4, pin_memory=True) if cuda else dict(shuffle=True, batch_size=64)\n",
        "\n",
        "\n",
        "\n",
        "# train dataloader\n",
        "train_loader = torch.utils.data.DataLoader(trainset, **dataloader_args)\n",
        " \n",
        "\n",
        "\n",
        "\n",
        "  # test dataloader\n",
        "test_loader = torch.utils.data.DataLoader(testset, **dataloader_args)\n",
        "\n",
        "\n",
        "\n",
        " "
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "f2s44SvP4yta",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": 0,
      "outputs": []
    }
  ]
}

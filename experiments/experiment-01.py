from torchvision.models import detection
import numpy as np
import torch
import cv2

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

DEVICE
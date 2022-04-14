import os.path
import random
import math
import cv2
import numpy
import matplotlib.pyplot as plt
from PIL import Image

from DataAugmentationAPI import DataAugmentationAPI

test = DataAugmentationAPI()
test.setSourceDirectory()
test.setDestinationDirectory()
test.Print()
test.generateAugmentedImages(None)
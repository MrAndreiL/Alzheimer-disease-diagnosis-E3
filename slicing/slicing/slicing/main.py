from __future__ import absolute_import, division, print_function, unicode_literals

import os

import numpy as np

import SimpleITK as sitk
from matplotlib import pyplot as plt

import cv2

import sys


def slice(path, output_path_results, output_path_slices):
    index = 0
    for imagePath in os.listdir(path):
        # imagePath contains name of the image
        image_path = os.path.join(path, imagePath)

        image_sitk = sitk.ReadImage(image_path, sitk.sitkFloat32)
        image = sitk.GetArrayFromImage(image_sitk)
        print("image" + str(index) + "={}".format(image.shape))

        depth = image.shape[0]

        f, axarr = plt.subplots(1, depth, figsize=(20, 20))
        i = 0
        for x in axarr:
            x.imshow(np.squeeze(image[i, :, :]), cmap='gray', origin='lower')
            my_slice_path = str(index) + "\\" + "slice" + str(i) + ".png"
            os.makedirs(os.path.dirname(os.path.join(output_path_slices, my_slice_path)), exist_ok=True)
            with open(os.path.join(output_path_slices, my_slice_path), "w") as f:
                f.write("my_slice_path")
            cv2.imwrite(os.path.join(output_path_slices, my_slice_path), image[i, :, :])
            x.set_xticks([])
            x.set_yticks([])
            i = i + 1
        plt.tight_layout()
        plt.subplots_adjust(wspace=0, hspace=0)
        my_image_path = str(index) + "result.svg"
        plt.savefig(os.path.join(output_path_results, my_image_path), dpi=1200)
        # plt.show()
        index = index + 1
if len(sys.argv) > 1:
    path = sys.argv[1]
    output_path_results = sys.argv[2]
    output_path_slices = sys.argv[3]
    slice(path, output_path_results, output_path_slices)
else:
    print("provide parameters")
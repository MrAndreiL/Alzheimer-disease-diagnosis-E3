from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
import numpy as np
import pandas as pd
import SimpleITK as sitk
from matplotlib import pyplot as plt
from scipy.ndimage import map_coordinates
from scipy.ndimage import gaussian_filter
from scipy import ndimage
import math
from skimage.filters import threshold_mean
import cv2

ct_path = 'C:/Users/Rogue EX/Desktop/resurse/sub-OAS30001_sess-d0757_task-rest_run-02_bold.nii'
ct_label_path = 'C:/Users/Rogue EX/Desktop/resurse/sub-OAS30001_sess-d0757_task-rest_run-02_bold.nii'
exemplu_path = 'C:/Users/Rogue EX/Desktop/resurse/sub-OAS30001_sess-d0757_task-rest_run-02_bold.nii'
exemplu_path2 = 'C:/Users/Rogue EX/Desktop/resurse/sub-OAS30001_sess-d0757_minIP.nii'

# CT
img_sitk = sitk.ReadImage(ct_path, sitk.sitkFloat32)  # Reading CT
image = sitk.GetArrayFromImage(img_sitk)  # Converting sitk_metadata to image Array
# Mask
mask_sitk = sitk.ReadImage(ct_label_path, sitk.sitkInt32)  # Reading CT
mask = sitk.GetArrayFromImage(mask_sitk)  # Converting sitk_metadata to image Array

# arhiva1
exemplu_sitk = sitk.ReadImage(exemplu_path, sitk.sitkFloat32)
exemplu = sitk.GetArrayFromImage(exemplu_sitk)

#arhiva2
exemplu2_sitk = sitk.ReadImage(exemplu_path2, sitk.sitkFloat32)
exemplu2 = sitk.GetArrayFromImage(exemplu2_sitk)

print('CT Shape={}'.format(image.shape))
print('CT Mask Shape={}'.format(mask.shape))
print('CT Altceva Shape={}'.format(exemplu.shape))
print('exemplu2={}'.format(exemplu2.shape))
"""
f, axarr = plt.subplots(1, 5, figsize=(20, 20))
axarr[0].imshow(np.squeeze(image[100, :, :]), cmap='gray', origin='lower');
axarr[0].set_ylabel('Axial View', fontsize=14)
axarr[0].set_xticks([])
axarr[0].set_yticks([])
axarr[0].set_title('CT', fontsize=14)

axarr[1].imshow(np.squeeze(mask[100, :, :]), cmap='jet', origin='lower');
axarr[1].axis('off')
axarr[1].set_title('Mask', fontsize=14)

axarr[2].imshow(np.squeeze(image[100, :, :]), cmap='gray', alpha=1, origin='lower');
axarr[2].imshow(np.squeeze(mask[100, :, :]), cmap='jet', alpha=0.5, origin='lower');
axarr[2].axis('off')
axarr[2].set_title('Overlay', fontsize=14)

axarr[3].imshow(np.squeeze(exemplu[32, :, :]), cmap='gray', origin='lower');
axarr[3].set_xticks([])
axarr[3].set_yticks([])
axarr[3].set_title('Exemplu din arhiva', fontsize=14)

axarr[4].imshow(np.squeeze(exemplu2[1, :, :]), cmap='gray', origin='lower');
axarr[4].set_xticks([])
axarr[4].set_yticks([])
axarr[4].set_title('Exemplu din arhiva 2', fontsize=14)
"""

f, axarr2 = plt.subplots(1, 72, figsize=(20, 20))
i=1
for x in axarr2:
    x.imshow(np.squeeze(exemplu2[i, :, :]), cmap='gray', origin='lower');
    x.set_xticks([])
    x.set_yticks([])
    i=i+1

plt.tight_layout()
plt.subplots_adjust(wspace=0, hspace=0)
plt.show(interpolation='nearest', aspect='auto')


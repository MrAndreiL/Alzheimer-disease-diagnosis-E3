import cv2
import glob
import os.path
import numpy


def compare(image1, image2):

    res = cv2.absdiff(image1, image2)

    res = res.astype(numpy.uint8)

    percentage = (numpy.count_nonzero(res) * 100) / res.size

    return percentage


imdir = 'brainsToCompareWith'
imdir2 = 'brainsFromSlicing'
ext = ['png', 'jpg', 'gif']

files = []
[files.extend(glob.glob(imdir + '*.' + e)) for e in ext]

files2 = []
[files.extend(glob.glob(imdir2 + '*.' + e)) for e in ext]
#problema
imagesToCompareWith = [cv2.imread(file) for file in files]
imagesFromSlicing = [cv2.imread(file) for file in files2]

i = 0
for img1 in imagesFromSlicing:
    flag = 0
    for img2 in imagesToCompareWith:
        if compare(img1, img2) < 20:
            flag = 1
    if flag == 1:
        i = i + 1
        cv2.imwrite(os.path.join('C:/Users/Rogue EX/Desktop/relevant/resources', 'brain' +
                                 i + '.jpg'), img1)
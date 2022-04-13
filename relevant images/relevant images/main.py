import cv2
import glob
import os.path
import numpy
from skimage import io


def compare(image1, image2):

    res = cv2.absdiff(image1, image2)

    res = res.astype(numpy.uint8)

    percentage = (numpy.count_nonzero(res) * 100) / res.size

    return percentage


def createArrays(imagesToCompareWith, imagesFromSlicing):
    file_list = glob.glob(
        r'C:\Users\Rogue EX\Desktop\relevant\brainsToCompareWith\*.*'
    )
    file_list2 = glob.glob(
        r'C:\Users\Rogue EX\Desktop\relevant\brainsFromSlicing\*.*'
    )

    for file in file_list:
        im = io.imread(file)
        imagesToCompareWith.append(im)

    for file in file_list2:
        im = io.imread(file)
        imagesFromSlicing.append(im)


def chooseRelevantImages(imagesToSelectFrom, imagesToCompareWith):
    numberOfPhoto = 0
    for img1 in imagesToSelectFrom:
        flag = 0
        for img2 in imagesToCompareWith:
            if compare(img1, img2) < 20:
                flag = 1
        if flag == 1:
            numberOfPhoto = numberOfPhoto + 1
            cv2.imwrite(os.path.join(r'C:\Users\Rogue EX\Desktop\relevant\new brains', 'brain' +
                                     str(numberOfPhoto) + '.jpg'), img1)


imagesToCompareWith = []
imagesFromSlicing = []
createArrays(imagesToCompareWith, imagesFromSlicing)
chooseRelevantImages(imagesFromSlicing, imagesToCompareWith)
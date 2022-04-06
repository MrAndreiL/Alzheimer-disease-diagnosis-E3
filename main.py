# Import required Image library

import glob
import shutil
import random
import os
import PIL
from PIL import Image, ImageFilter, ImageEnhance
from PIL.ImageOps import mirror


# Method to get the image
def getImage(path):
    OriImage = Image.open(path)
    # OriImage.show()
    return OriImage


# Method to blur the image
def gaussianBlur(image):
    blurImage = image.filter(ImageFilter.BLUR)
    # blurImage.show()
    return blurImage


# Method to rotate the image
def rotate(image, x):
    rotated = image.rotate(x)
    # rotated.show()
    return rotated


# Method to flip the image
def flip(image, varianta):
    if varianta == "flip":
        fliped = PIL.ImageOps.flip(image)
    elif varianta == "mirror":
        fliped = PIL.ImageOps.mirror(image)
    # fliped.show()
    return fliped


# Method to stretch the image
def imageStretch(image, horizontal, vertical):
    stretched = image.resize((round(image.size[0] * (1 + horizontal)), round(image.size[1] * (1 + vertical))))
    # stretched.show()
    return stretched


# Method to Crop the image
def imageCrop(image, x1, y1, x2, y2):
    croped = image.crop((x1, y1, x2, y2))
    # croped.show()
    return croped


# Method to increase the image
def contrast(image, contrast):
    enhancer = ImageEnhance.Contrast(image)
    contrasted = enhancer.enhance(contrast)
    # contrasted.show()
    return contrasted


# Method to save the image
def addImage(image, varianta, nr_folder):
    if nr_folder > 0:
        nr = str(nr_folder)
    else:
        nr = ""
    match varianta:
        case 'blur':
            path = 'Augmented/brain' + nr + '/blurred.png'
            i = 1
            while (os.path.isfile(path)):
                path = 'Augmented/brain' + nr + '/blurred' + str(i) + '.png'
                i = i + 1
            image.save(path)
        case 'rotate':
            path = 'Augmented/brain' + nr + '/rotate.png'
            i = 1
            while (os.path.isfile(path)):
                path = 'Augmented/brain' + nr + '/rotate' + str(i) + '.png'
                i = i + 1
            image.save(path)
        case 'flip':
            path = 'Augmented/brain' + nr + '/fliped.png'
            i = 1
            while (os.path.isfile(path)):
                path = 'Augmented/brain' + nr + '/fliped' + str(i) + '.png'
                i = i + 1
            image.save(path)
        case 'stretch':
            path = 'Augmented/brain' + nr + '/stretched.png'
            i = 1
            while (os.path.isfile(path)):
                path = 'Augmented/brain' + nr + '/stretched' + str(i) + '.png'
                i = i + 1
            image.save(path)
        case 'crop':
            path = 'Augmented/brain' + nr + '/croped.png'
            i = 1
            while (os.path.isfile(path)):
                path = 'Augmented/brain' + nr + '/croped' + str(i) + '.png'
                i = i + 1
            image.save(path)
        case 'contrast':
            path = 'Augmented/brain' + nr + '/contrasted.png'
            i = 1
            while (os.path.isfile(path)):
                path = 'Augmented/brain' + nr + '/contrasted' + str(i) + '.png'
                i = i + 1
            image.save(path)


def generateAugmentedImages():
    i = 0
    path = "Original/brain.png"
    while (os.path.isfile(path)):
        image = getImage(path)
        try:
            if i > 0:
                os.mkdir("Augmented/brain" + str(i))
                shutil.copy(path, "Augmented/brain" + str(i))
            else:
                os.mkdir("Augmented/brain")
                shutil.copy(path, "Augmented/brain")
        except FileExistsError:
            if i == 0:
                print("Folder brain already exists!")
            else:
                print("Folder brain" + str(i) + " already exists!")

        for j in range(10):
            augmented_image = image
            for k in range(10):
                x = random.randint(1, 6)
                match x:
                    case 1:
                        augmented_image = gaussianBlur(augmented_image)
                        addImage(augmented_image, 'blur', i)
                    case 2:
                        augmented_image = rotate(augmented_image, random.randint(1, 180))
                        addImage(augmented_image, 'rotate', i)
                    case 3:
                        rand = random.randint(1, 2)
                        if rand == 1:
                            augmented_image = flip(augmented_image, 'flip')
                            addImage(augmented_image, 'flip', i)
                        else:
                            augmented_image = flip(augmented_image, 'mirror')
                            addImage(augmented_image, 'flip', i)
                    case 4:
                        horizontal = float(str("0." + str(random.randint(1, 12))))
                        vertical = float(str("0." + str(random.randint(1, 12))))
                        augmented_image = imageStretch(augmented_image, horizontal, vertical)
                        addImage(augmented_image, 'stretch', i)
                    case 5:
                        h, w = augmented_image.size
                        x1 = random.randint(1, w)
                        x2 = random.randint(x1 + 1, x1 + w)
                        y1 = random.randint(1, h)
                        y2 = random.randint(y1 + 1, y1 + h)
                        augmented_image = imageCrop(augmented_image, x1, y1, x2, y2)
                        addImage(augmented_image, 'crop', i)
                    case 6:
                        rand = float(str("0." + str(random.randint(1, 10))))
                        augmented_image = contrast(augmented_image, rand)
                        addImage(augmented_image, 'contrast', i)
        os.remove(path)
        i = i + 1
        path = "Original/brain" + str(i) + ".png"

generateAugmentedImages()
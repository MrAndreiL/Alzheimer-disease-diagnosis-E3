# Required Libraries
import glob

import matplotlib.pyplot as plt
import shutil
import random
import os
import PIL
import numpy
import cv2
from PIL import Image, ImageFilter, ImageEnhance
from PIL.ImageOps import mirror


class DataAugmentationAPI:
    source = None
    destination = None

    def __init__(self):
        pass

    def Print(self):
        try:
            print('Source path is:' + self.source)
            print('Destination path is:' + self.destination)
        except TypeError:
            print('Source path does not exist')
            print('Destination path does not exist')

    def setSourceDirectory(self):
        folder = input('Folder name for the images: ')
        path = os.getcwd() + '\\' + folder
        while not (os.path.exists(path)):
            if not (os.path.exists(path)):
                print('\033[93m' + 'Folder doesnt exist' + '\033[0m')
            folder = input('Folder name for the images: ')
            path = os.getcwd() + '\\' + folder
        # print(path)
        self.source = path

    def setDestinationDirectory(self):
        folder = input('Folder name to put images in: ')
        path = os.getcwd() + '\\' + folder
        while not (os.path.exists(path)):
            if not (os.path.exists(path)):
                print('\033[93m' + 'Folder doesnt exist' + '\033[0m')
            folder = input('Folder name to put images in: ')
            path = os.getcwd() + '\\' + folder
        # print(path)
        self.destination = path

    # Method to get the image from path
    def getImage(self, path):
        image = Image.open(path)
        return image

    # Method to blur the image
    def gaussianBlur(self, image):
        blurImage = image.filter(ImageFilter.BLUR)
        return blurImage

    # Method to rotate the image
    def rotate(self, image, x):
        rotated = image.rotate(x, expand=True)
        return rotated

    # Method to flip the image
    def flip(self, image, varianta):
        if varianta == "flip":
            fliped = PIL.ImageOps.flip(image)
        elif varianta == "mirror":
            fliped = PIL.ImageOps.mirror(image)
        return fliped

    # Method to stretch the image
    def imageStretch(self, image, horizontal, vertical):
        stretched = image.resize((round(image.size[0] * (1 + horizontal)), round(image.size[1] * (1 + vertical))))
        return stretched

    # Method to Crop the image
    def imageCrop(self, image, x1, y1, x2, y2):
        croped = image.crop((x1, y1, x2, y2))
        return croped

    def centerCrop(self, image):
        w, h = image.size
        cv_img = numpy.asarray(image)
        gray = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, threshold1=75, threshold2=100)
        y_up = h
        y_down = 0
        x_left = w
        x_right = 0
        indices = numpy.where(edges != [0])
        for i in range(indices[0].size):
            if (indices[0][i] > 5 and indices[1][i] > 15) and (
                    indices[0][i] < h - 5 and indices[1][i] < w - 15):
                if indices[0][i] < y_up:
                    y_up = indices[0][i]
                elif indices[0][i] > y_down:
                    y_down = indices[0][i]
                elif indices[1][i] < x_left:
                    x_left = indices[1][i]
                elif indices[1][i] > x_right:
                    x_right = indices[1][i]

        image = Image.fromarray(cv_img)
        try:
            image = self.imageCrop(image, x_left, y_up, x_right, y_down)
            image = image.resize((w, h))
        except ValueError:
            if x_left > x_right:
                aux = x_left
                x_left = x_right
                x_right = aux
            if y_up > y_down:
                aux = y_up
                y_up = y_down
                y_down = aux
            image = self.imageCrop(image, x_left, y_up, x_right, y_down)
            image = image.resize((w, h))
        return image

    # Method to modify the contrast
    def contrast(self, image, contrast):
        enhancer = ImageEnhance.Contrast(image)
        contrasted = enhancer.enhance(contrast)
        return contrasted

    # Method to save the image
    def addImage(self, image, varianta, filename):
        match varianta:
            case 'blur':
                path = filename + '\\blurred.png'
                i = 1
                while os.path.isfile(path):
                    path = filename + '\\blurred' + str(i) + '.png'
                    i = i + 1
                image.save(path)
            case 'rotate':
                path = filename + '\\rotate.png'
                i = 1
                while os.path.isfile(path):
                    path = filename + '\\rotate' + str(i) + '.png'
                    i = i + 1
                image.save(path)
            case 'flip':
                path = filename + '\\flipped.png'
                i = 1
                while os.path.isfile(path):
                    path = filename + '\\flipped' + str(i) + '.png'
                    i = i + 1
                image.save(path)
            case 'mirror':
                path = filename + '\\mirrored.png'
                i = 1
                while os.path.isfile(path):
                    path = filename + '\\mirrored' + str(i) + '.png'
                    i = i + 1
                image.save(path)
            case 'stretch':
                path = filename + '\\stretched.png'
                i = 1
                while os.path.isfile(path):
                    path = filename + '\\stretched' + str(i) + '.png'
                    i = i + 1
                image.save(path)
            case 'crop':
                path = filename + '\\cropped.png'
                i = 1
                while os.path.isfile(path):
                    path = filename + '\\cropped' + str(i) + '.png'
                    i = i + 1
                image.save(path)
            case 'contrast':
                path = filename + '\\contrasted.png'
                i = 1
                while os.path.isfile(path):
                    path = filename + '\\contrasted' + str(i) + '.png'
                    i = i + 1
                image.save(path)

    def cropRemake(self, image, augmented_image, augments_order, rotate_angle, stretchx, stretchy, contrast_level):
        for x in augments_order:
            match x:
                case 1:
                    augmented_image = self.gaussianBlur(augmented_image)
                    # self.addImage(augmented_image, 'crop', (image.filename.split('\\')[-1])[:-4])
                case 2:
                    augmented_image = self.rotate(augmented_image, rotate_angle)
                    # self.addImage(augmented_image, 'crop', (image.filename.split('\\')[-1])[:-4])
                case 3:
                    augmented_image = self.flip(augmented_image, 'flip')
                    # self.addImage(augmented_image, 'crop', (image.filename.split('\\')[-1])[:-4])
                case 4:
                    augmented_image = self.flip(augmented_image, 'mirror')
                    # self.addImage(augmented_image, 'crop', (image.filename.split('\\')[-1])[:-4])
                case 5:
                    augmented_image = self.imageStretch(augmented_image, stretchx, stretchy)
                    # self.addImage(augmented_image, 'crop', (image.filename.split('\\')[-1])[:-4])
                case 7:
                    augmented_image = self.contrast(augmented_image, contrast_level)
                    # self.addImage(augmented_image, 'crop', (image.filename.split('\\')[-1])[:-4])
                case _:
                    pass
        return augmented_image

    def randomAugments(self, image, save_location):
        for j in range(10):
            augmented_image = image
            # plt.imshow(augmented_image)
            # plt.show()
            augments_done = {'blur': 0, 'rotate': 0, 'flip': 0, 'mirror': 0, 'stretch': 0, 'crop': 0, 'contrast': 0}
            k = 0
            augments_order = []
            angle = 0
            rand = 0
            horizontal = 0
            vertical = 0
            while k < 7:
                x = random.randint(1, 7)
                match x:
                    case 1:
                        if augments_done['blur'] == 1:
                            pass
                        else:
                            k = k + 1
                            augments_order.append(x)
                            augments_done['blur'] = 1
                            augmented_image = self.gaussianBlur(augmented_image)
                            self.addImage(augmented_image, 'blur', save_location)
                            # plt.imshow(augmented_image)
                            # plt.show()
                    case 2:
                        if augments_done['rotate'] == 1:
                            pass
                        else:
                            k = k + 1
                            augments_order.append(x)
                            augments_done['rotate'] = 1
                            angle = random.randint(-25, 25)
                            augmented_image = self.rotate(augmented_image, angle)
                            self.addImage(augmented_image, 'rotate', save_location)
                            # plt.imshow(augmented_image)
                            # plt.show()
                    case 3:
                        if augments_done['flip'] == 1:
                            pass
                        else:
                            k = k + 1
                            augments_order.append(x)
                            augments_done['flip'] = 1
                            augmented_image = self.flip(augmented_image, 'flip')
                            self.addImage(augmented_image, 'flip', save_location)
                            # plt.imshow(augmented_image)
                            # plt.show()
                    case 4:
                        if augments_done['mirror'] == 1:
                            pass
                        else:
                            k = k + 1
                            augments_order.append(x)
                            augments_done['mirror'] = 1
                            augmented_image = self.flip(augmented_image, 'mirror')
                            self.addImage(augmented_image, 'mirror', save_location)
                            # plt.imshow(augmented_image)
                            # plt.show()
                    case 5:
                        if augments_done['stretch'] == 1:
                            pass
                        else:
                            k = k + 1
                            augments_order.append(x)
                            augments_done['stretch'] = 1
                            horizontal = float(f'{random.uniform(0.1, 0.5):.1f}')
                            vertical = float(f'{random.uniform(0.1, 0.5):.1f}')
                            augmented_image = self.imageStretch(augmented_image, horizontal, vertical)
                            self.addImage(augmented_image, 'stretch', save_location)
                            # plt.imshow(augmented_image)
                            # plt.show()
                    case 6:
                        if augments_done['crop'] == 1:
                            pass
                        else:
                            k = k + 1
                            augments_done['crop'] = 1
                            augmented_image = self.centerCrop(image)
                            # self.addImage(augmented_image, 'crop', (image.filename.split('\\')[-1])[:-4])
                            if k > 1:
                                augmented_image = self.cropRemake(image, augmented_image, augments_order, angle,
                                                                  horizontal,
                                                                  vertical, rand)
                            self.addImage(augmented_image, 'crop', save_location)
                    case 7:
                        if augments_done['contrast'] == 1:
                            pass
                        else:
                            augments_done['contrast'] = 1
                            k = k + 1
                            augments_order.append(x)
                            rand = float(f'{random.uniform(0.5, 1.5):.1f}')
                            while rand == 1.0:
                                rand = float(f'{random.uniform(0.5, 1.5):.1f}')
                            augmented_image = self.contrast(augmented_image, rand)
                            self.addImage(augmented_image, 'contrast', save_location)
                            # plt.imshow(augmented_image)
                            # plt.show()

    def removeOriginalFiles(self, mode='DEFAULT'):
        answer = {'remove': False, 'copy': True}
        if mode == 'DEFAULT':
            pass
        else:
            print('Answer with YES/NO or DA/NU or DEFAULT, not case sensitive')
            answer1 = input('Do you want to remove the original images?: ')
            while answer1.upper() not in {'YES', 'NO', 'DA', 'NU', 'DEFAULT'}:
                answer1 = input('\033[91m' + 'Choose between YES/NO or DA/NU or DEFAULT:' + '\033[0m ')
            answer2 = input('Do you want to copy the original images in the augmented images folders?: ')
            while answer2.upper() not in {'YES', 'NO', 'DA', 'NU', 'DEFAULT'}:
                answer2 = input('\033[91m' + 'Choose between YES/NO or DA/NU or DEFAULT:' + '\033[0m ')
            if answer1.upper() == 'YES' or answer1.upper() == 'DA':
                answer['remove'] = True
            if answer2.upper() == 'NO' or answer2.upper() == 'NU':
                answer['copy'] = False
        return answer

    def generateAugmentedImages(self, mode='DEFAULT'):
        if mode == 'DEFAULT':
            preference = self.removeOriginalFiles()
        else:
            preference = self.removeOriginalFiles(None)
        directories = os.listdir(self.source)
        if self.source == self.destination:
            for dir in directories:
                if ('_Augmented' in dir) is True:
                    shutil.rmtree(os.path.join(self.source,dir))
        else:
            directories_dest = os.listdir(self.destination)
            for dir in directories_dest:
                if ('_Augmented' in dir) is True:
                    shutil.rmtree(os.path.join(self.destination,dir))
        directories = os.listdir(self.source)
        for dir in directories:
            path_original = os.path.join(self.source, dir)
            path_destination = os.path.join(self.destination, dir)
            path_destination = path_destination + '_Augmented'
            os.mkdir(path_destination)
            print(path_original.split('\\')[-1]+'... ', end="")
            for file in glob.glob(path_original + '\\*.png'):
                image = self.getImage(file)
                if preference['copy'] is True:
                    shutil.copy(file, path_destination + '\\' + (
                        image.filename.split('\\')[-1]))
                self.randomAugments(image, path_destination)
                if preference['remove'] is True:
                    os.remove(file)
            print(path_destination.split('\\')[-1])

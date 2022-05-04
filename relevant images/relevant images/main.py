from email.mime import image
import cv2
import numpy as np
import glob


class RelevantImages():
    imagesFromSlicing = []
    imagesToCompareWith = []

    def __init__(self,path1, path2) -> None:
        self.imagesFromSlicing = [cv2.imread(file) for file in glob.glob(f'{path1}/*.png')]
        self.imagesToCompareWith = [cv2.imread(file) for file in glob.glob(f'{path2}/*.png')]

    def compare(self,image1, image2):
        sift = cv2.xfeatures2d.SIFT_create()
        kp_1, desc_1 = sift.detectAndCompute(image1, None)
        kp_2, desc_2 = sift.detectAndCompute(image2, None)

        index_params = dict(algorithm=0, trees=5)
        search_params = dict()
        flann = cv2.FlannBasedMatcher(index_params, search_params)

        matches = flann.knnMatch(desc_1, desc_2, k=2)

        good_points = []
        for m, n in matches:
            if m.distance < 0.6*n.distance:
                good_points.append(m)

        number_keypoints = 0
        if len(kp_1) <= len(kp_2):
            number_keypoints = len(kp_1)
        else:
            number_keypoints = len(kp_2)

        print("% comparare: ", len(good_points) / number_keypoints * 100)

        return len(good_points) / number_keypoints * 100

    def compareAll(self):
        numberOfPhoto = 0
        pathFinal = r'C:\Users\Rogue EX\Desktop\relevant\new brains\a'
        for image in self.imagesFromSlicing:
            flag = 0
            for image2 in self.imagesToCompareWith:
                result = self.compare(image, image2)
                if result > 2.0:
                    flag = 1
                    break
            if(flag == 1):
                numberOfPhoto += 1
                cv2.imwrite(f'{pathFinal}{"Brain" + str(numberOfPhoto)}.png',image)
        return numberOfPhoto

path1 = r'C:\Users\Rogue EX\Desktop\relevant\brainsFromSlicing'
path2 = r'C:\Users\Rogue EX\Desktop\relevant\brainsToCompare'

scanner = RelevantImages(path1,path2)
print(scanner.compareAll())


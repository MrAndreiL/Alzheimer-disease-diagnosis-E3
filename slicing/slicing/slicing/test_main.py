import os
from unittest import TestCase
from main import slice
from comparesvg import validate_file_contents
import cv2
from PIL import Image
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

class Test(TestCase):
    # 3 teste, pe rand unul dintre foldere nu exista
    def test_slice_inexistent1(self):
        path = 'C:\\Users\\cezar\\Desktop\\ip\\Project\\inexistent'
        output_path_results = 'C:\\Users\\cezar\\Desktop\\ip\\Project\\results'
        output_path_slices = 'C:\\Users\\cezar\\Desktop\\ip\\Project\slices'
        self.assertEqual(False, slice(path, output_path_results, output_path_slices))

    def test_slice_inexistent2(self):
        path = 'C:\\Users\\cezar\\Desktop\\ip\\Project\\resources'
        output_path_results = 'C:\\Users\\cezar\\Desktop\\ip\\Project\\inexistent'
        output_path_slices = 'C:\\Users\\cezar\\Desktop\\ip\\Project\slices'
        self.assertEqual(False, slice(path, output_path_results, output_path_slices))

    def test_slice_inexistent3(self):
        path = 'C:\\Users\\cezar\\Desktop\\ip\\Project\\resources'
        output_path_results = 'C:\\Users\\cezar\\Desktop\\ip\\Project\\results'
        output_path_slices = 'C:\\Users\\cezar\\Desktop\\ip\\Project\inexistent'
        self.assertEqual(False, slice(path, output_path_results, output_path_slices))

    def test_slice_valid(self):
        path = 'C:\\Users\\cezar\\Desktop\\ip\\Project\\resources2'
        output_path_results = 'C:\\Users\\cezar\\Desktop\\ip\\Project\\results'
        output_path_slices = 'C:\\Users\\cezar\\Desktop\\ip\\Project\slices'
        self.assertEqual(True, slice(path, output_path_results, output_path_slices))
"""
    def test_slice_compare(self):
        path = 'C:\\Users\\cezar\\Desktop\\ip\\Project\\resources'
        output_path_results = 'C:\\Users\\cezar\\Desktop\\ip\\Project\\results2'
        output_path_slices = 'C:\\Users\\cezar\\Desktop\\ip\\Project\slices'
        slice(path, output_path_results, output_path_slices)
        for imagePath1 in os.listdir('C:\\Users\\cezar\\Desktop\\ip\\Project\\results2'):
            absPath1 = os.path.abspath('results2\\' + imagePath1)
            for imagePath2 in os.listdir('C:\\Users\\cezar\\Desktop\\ip\\Project\\results'):
                absPath2 = os.path.abspath('results\\' + imagePath2)
                if imagePath1 == imagePath2:
                    drawing1 = svg2rlg(absPath1)
                    drawing2 = svg2rlg(absPath2)
                    renderPM.drawToFile(drawing1, 'test.png', fmt="PNG")
                    renderPM.drawToFile(drawing2, 'test2.png', fmt="PNG")
                    im1 = Image.open('test.png')
                    im2 = Image.open('test2.png')
                    if not validate_file_contents(im1, im2) :
                        assert False
                    break
"""

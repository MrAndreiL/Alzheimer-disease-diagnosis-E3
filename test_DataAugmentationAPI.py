from unittest import TestCase

from DataAugmentationAPI import DataAugmentationAPI

test = DataAugmentationAPI()

class TestDataAugmentationAPI(TestCase):
    image = test.getImage("brain.png")
    def test_gaussian_blur(self):
        # image = test.getImage("brain.png")
        blurred = test.gaussianBlur(self.image)
        blurred.save("input\\blurred.png")
        blurred = test.getImage("input\\blurred.png")
        blurred_already = test.getImage("expected_output\\blur.png")
        self.assertEqual(blurred,blurred_already)

    def test_rotate(self):
        # image = test.getImage("brain.png")
        rotated = test.rotate(self.image,45)
        rotated.save("input\\rotated.png")
        rotated = test.getImage("input\\rotated.png")
        rotated_already = test.getImage("expected_output\\rotate45.png")
        self.assertEqual(rotated, rotated_already)

    def test_flip(self):
        # image = test.getImage("brain.png")
        flip = test.flip(self.image,'flip')
        flip.save("input\\flip.png")
        flip = test.getImage("input\\flip.png")
        flip_already = test.getImage("expected_output\\flip.png")
        self.assertEqual(flip, flip_already)

    def test_image_stretch(self):
        # image = test.getImage("brain.png")
        stretch = test.imageStretch(self.image,1,1)
        stretch.save("input\\stretch.png")
        stretch = test.getImage("input\\stretch.png")
        stretch_already = test.getImage("expected_output\\stretch1_1.png")
        self.assertEqual(stretch, stretch_already)

    def test_image_crop(self):
        # image = test.getImage("brain.png")
        crop = test.imageCrop(self.image,20,20,40,40)
        crop.save("input\\crop.png")
        crop = test.getImage("input\\crop.png")
        crop_already = test.getImage("expected_output\\crop20204040.png")
        self.assertEqual(crop,crop_already)

    def test_contrast(self):
        # image = test.getImage("brain.png")
        contrast = test.contrast(self.image,1)
        contrast.save("input\\contrast.png")
        contrast = test.getImage("input\\contrast.png")
        contrast_already = test.getImage("expected_output\\contrast1.png")
        self.assertEqual(contrast, contrast_already)

    def parameterTesting():
        ok = True

        for i in range(0,100):
            rotate_param = random.randint(-25, 25)
            if not (rotate_param in range(-25,25)):
                ok = False

            stretch_param = random.randint(1, 5)
            if not (rotate_param in range(1, 5)):
                ok = False
        if ok:
            return True
        else:
            return False


    class TestDataAugmentationAPI2(TestCase):
        def test(self):
            self.assertEqual(parameterTesting(),True)
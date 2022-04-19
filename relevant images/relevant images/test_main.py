import unittest
import relevantImages

class TestRelevantImages(unittest.TestCase):
    path1 = r'brainsFromSlicing'
    path2 = r'brainsToCompareWith'
    scanner = relevantImages.RelevantImages(path1,path2)

    def test_compare(self):
        self.assertGreaterEqual(0, self.scanner.compare(self.scanner.imagesFromSlicing[0], self.scanner.imagesToComparaeWith[0]))

    def test_compareAll(self):
        self.assertGreaterEqual(1, self.scanner.compareAll())


if __name__ == '__main__':
    unittest.main()
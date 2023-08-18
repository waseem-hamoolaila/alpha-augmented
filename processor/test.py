from django import test

from .fitting_utils import Package, Box


class TestFittingEngine(test.TestCase):
    def setUp(self):
        self.package = Package([[1, 1, 1], [0, 0, 1]])
        self.package2 = Package([[1, 1, 1, 0]])
        self.package3 = Package([[1, 1, 1], [0, 0, 1], [1, 1, 0]])

        self.box = Box(8, 8)

    def test_initial_package(self):
        self.assertEqual(self.package.rows, 2)
        self.assertEqual(self.package.cols, 3)

    def test_package_dimensions(self):
        self.assertEqual(len(self.package.structure), 2)
        self.assertEqual(len(self.package.structure[0]), 3)

    def test_initial_box(self):
        self.assertEqual(self.box.cols, 8)
        self.assertEqual(self.box.rows, 8)
        
    
    

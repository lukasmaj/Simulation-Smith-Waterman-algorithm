import os
import time
import SmithWaterman as sm_alg
import Algorithm2D as alg_2d
import img_utils as imgu

class TestClass:

    def __init__(self):
        print "Test Class"
        self.BImage = ['X', 'G', 'G', 'T', 'T', 'G', 'A', 'C', 'T', 'A'];
        self.AImage = ['Y', 'T', 'G', 'T', 'T', 'A', 'C', 'G', 'G'];

    def test(self):
        sm_alg.alignSequence(AImage=self.AImage, BImage=self.BImage)
        imgA, imgB = imgu.getImages()
        alg_2d.alignSequence(AImage2D=imgA, BImage2D=imgB)

if __name__ == "__main__":
    tc = TestClass()
    tc.test()

import cv2 as cv


class ImageUtils:

    def __init__(self):
        print "Init ImageUtils"

    def getImages(self):
        imgA = cv.imread('img/L.png', 0)

        imgB = cv.imread('img/P.png', 0)
        return imgA, imgB


__img_utils = ImageUtils()

getImages = __img_utils.getImages
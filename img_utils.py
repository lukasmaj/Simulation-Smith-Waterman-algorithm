import cv2 as cv


class ImageUtils:

    def __init__(self):
        print "Init ImageUtils"

    def getImages(self):
        imgA = cv.imread('img/imgA.png',0)
        a = imgA[60]
        b = len(a)
        c = a[5]
        imgB = cv.imread('img/imgB',0)



__img_utils = ImageUtils()

getImages = __img_utils.getImages
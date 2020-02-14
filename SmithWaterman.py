import os
import time
import utils

class SmithWatermanAlgorithm:

    def __init__(self):
        print "Smith-Waterman Algorithm"
        self.Wk = 2

    def fillScoringMatrix(self, AImage, BImage):
        n, m = len(AImage), len(BImage)
        scoringMatrix = utils.fillZeros(sizeX=n, sizeY=m)
        for i in range(1, m):
            for j in range(1, n):
                cross = self.scoringCross(scoringMatrix=scoringMatrix, n=j, m=i, AImage=AImage, BImage=BImage)
                up = self.scoringUp(scoringMatrix=scoringMatrix, n=j, m=i, Wk=self.Wk)
                left = self.scoringLeft(scoringMatrix=scoringMatrix, n=j, m=i, Wk=self.Wk)
                d = 0
                scoringMatrix[i][j] = max(cross, up, left, d)
        return scoringMatrix

    def scoringUp(self, scoringMatrix, n, m, Wk):
        ret = scoringMatrix[m-1][n]-Wk
        return ret

    def scoringLeft(self, scoringMatrix, n, m, Wk):
        ret = scoringMatrix[m][n-1]-Wk
        return ret
    def scoringCross(self, scoringMatrix, n, m, AImage, BImage):
        ret = scoringMatrix[m-1][n-1] + self.score(a=AImage[n], b=BImage[m])
        return ret

    def score(self, a, b):
        if a == b:
            return 3
        else:
            return -3

    def alignSequence(self, AImage, BImage):
        print "Align Sequence"
        ret = self.fillScoringMatrix(AImage=AImage, BImage=BImage)
        utils.exposeMatrix(ret)

__smAlgorithm = SmithWatermanAlgorithm()
alignSequence = __smAlgorithm.alignSequence
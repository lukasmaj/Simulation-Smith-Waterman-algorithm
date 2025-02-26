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

    def computeMaxScore(self,scoringMatrix):
        maxScore = 0
        n, m = len(scoringMatrix[0]), len(scoringMatrix)
        for i in range(0, m):
            for j in range(0, n):
                if scoringMatrix[i][j] > maxScore:
                    maxScore = scoringMatrix[i][j]
                    posA = j
                    posB = i
        return posA, posB

    def computeBacktrack(self, scoringMatrix, maxScore):
        posA, posB = maxScore
        seqence =[]

        while posA != 1 and posB != 1:
            up = scoringMatrix[posB-1][posA]
            left = scoringMatrix[posB-1][posA]
            cross = scoringMatrix[posB-1][posA-1]
            maxNexScore = max(up, left, cross)

            if cross == maxNexScore or (posA-1 == 1) or (posB == 1):
                seqence.append([posA, posB])
                posA = posA -1
                posB = posB -1
            elif up == maxNexScore:
                seqence.append([None, posB])
                posA = posA
                posB = posB - 1
            elif left == maxNexScore:
                seqence.append([posA, None])
                posA = posA -1
                posB = posB
        return seqence

    def score(self, a, b):
        if a == b:
            return 3
        else:
            return -3
    def exposeSequence(self, sequence, AImage, BImage):
        stra=""
        strb=""
        for s in sequence:
            a, b = s
            if a is not None:
                stra = stra + "{0}".format(AImage[a])
            else:
                stra = stra + "-"
            if b is not None:
                strb = strb + "{0}".format(BImage[b])
            else:
                strb = strb + "-"
        print stra[::-1]
        print strb[::-1]

    def alignSequence(self, AImage, BImage):
        print "Align Sequence"
        scoringMatrix = self.fillScoringMatrix(AImage=AImage, BImage=BImage)
        maxScore = self.computeMaxScore(scoringMatrix=scoringMatrix)
        findSequence = self.computeBacktrack(scoringMatrix=scoringMatrix, maxScore=maxScore)
        self.exposeSequence(sequence=findSequence, AImage=AImage, BImage=BImage)
        # utils.exposeMatrix(scoringMatrix)

__smAlgorithm = SmithWatermanAlgorithm()
alignSequence = __smAlgorithm.alignSequence
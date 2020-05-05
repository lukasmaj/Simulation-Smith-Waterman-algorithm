import os
import SmithWaterman as sm_alg

class Hirschberg:
    def __init__(self):
        print "Hirschberg Alghoritm"

    def alignSequence(self, AImage, BImage):

        return None

    def NWScore(self, X, Y):

        m, n = len(X), len(Y)
        score = [[0 for i in range(0, n+1)] for j in range(0, n + 1)]
        score[0][0]=0
        for j in range(1, n):
            score[0][j]=score[0][j-1] + self.Ins(Y[j]);
        for i in range(1, m):
            score[i][0]=score(i-1,0) + self.Del(X[i])
            for j in range(1,n):
                scoreSub = score[i - 1][j - 1] + self.Sub(X[i], Y[j])
                scoreDel = score[i - 1] [j] + self.Del(X[i])
                scoreIns = score[i][j - 1] + self.Ins(Y[j])
                score[i][j] = max(scoreSub, scoreDel, scoreIns)
            score[0] = score[1]
        return score(n)
    def hir(self, X, Y):
        Z = ""
        W = ""
        if len(X) == 0:
            for i in range(1, len(Y)):
                Z = Z + "-"
                W = W + Y[i]
        elif len(Y) == 0:
            for i in range(1, len(X)):
                Z = Z + X[i]
                W = W + "-"
        elif len(X) == 1 or len(Y) == 1:
            Z, W = sm_alg.alignSequence(AImage=X, BImage=Y)

    def Ins(self, x):

        return -2;

    def Del(self,X):

        return -2

    def Sub(self, x, y):

        if x == y:
            return 2
        else:
            return -1

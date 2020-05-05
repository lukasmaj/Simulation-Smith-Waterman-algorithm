class Utils:
    def fillZeros(self, sizeX, sizeY):
        matrix = [[0 for i in range(0, sizeX)] for j in range(0,sizeY)]
        return matrix

    def matrixToArray(self, matrix):
        m, n = matrix.shape
        array = []

        for i in range(0, m):
            for j in range(0, n):
                array.append(matrix[i][j])
        return array

    def arrayToMatrix(self, array, m,n):
        k = 0
        matrix = [[0 for i in range(0, m + 1)] for j in range(0, n + 1)]
        for j in range(0, m):
            for i in range(0, n):
                matrix[i][j] = array[k]
                k = k + 1
        return matrix

    def exposeMatrix(self, matrix):
        for m in matrix:
            print m

__utils = Utils()

fillZeros = __utils.fillZeros
exposeMatrix = __utils.exposeMatrix
matrixToArray = __utils.matrixToArray
arrayToMatrix = __utils.arrayToMatrix
class Utils:
    def fillZeros(self, sizeX, sizeY):
        matrix = [[0 for i in range(0, sizeX)] for j in range(0,sizeY)]
        return matrix

    def exposeMatrix(self, matrix):
        for m in matrix:
            print m

__utils = Utils()

fillZeros = __utils.fillZeros
exposeMatrix = __utils.exposeMatrix
class Solution(object):
    def generateMatrix(self, n):
        matrix = [[0]*n for _ in range(n)]
        coordinates = [[[i,j] for j in range(n)] for i in range(n)]
        value = 1
        while coordinates:
            for i, j in coordinates.pop(0):
                matrix[i][j] = value
                value += 1
            coordinates = list(zip(*coordinates))[::-1]
        return matrix
        

if __name__ == '__main__':
    solution = Solution()
    n = 4
    matrix = solution.generateMatrix(4)
    print(matrix)
class Solution(object):
    def rotate(self, matrix):
        N_row, N_column = len(matrix), len(matrix[0])
        for i in range(N_row//2):
            k = N_row - 1 - i
            matrix[i], matrix[k] = matrix[k], matrix[i]
        for i in range(N_row):    
            for j in range(i+1):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        

if __name__ == '__main__':
    solution = Solution()
    testCase = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    solution.rotate(testCase)
    print(testCase)
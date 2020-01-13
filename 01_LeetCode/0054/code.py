class Solution(object):
    def spiralOrder(self, matrix):
        result_list = []
        while len(matrix):
            # top 
            result_list += matrix.pop(0)
            # right
            if matrix and matrix[0]:
                for row in matrix:
                    result_list.append(row.pop())
            # bottom
            if matrix:
                result_list += matrix.pop()[::-1]
            # left
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    result_list.append(row.pop(0))
        return result_list
        

if __name__ == '__main__':
    solution = Solution()
    testCase_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result_list = solution.spiralOrder(testCase_1)
    print(result_list)
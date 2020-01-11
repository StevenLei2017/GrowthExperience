class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        record_set = set()
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j] != '.':
                    value = board[i][j]
                    tuple_1 = (i, value)
                    tuple_2 = (value, j)
                    tuple_3 = (i//3, j//3, value)
                    if tuple_1 in record_set or tuple_2 in record_set or tuple_3 in record_set:
                        return False
                    record_set.add(tuple_1)
                    record_set.add(tuple_2)
                    record_set.add(tuple_3)
        return True
        

if __name__ == '__main__':
    solution = Solution()
    board = [[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],
        ["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],
        [".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]]
    result = solution.isValidSudoku(board)
    print(result)
    
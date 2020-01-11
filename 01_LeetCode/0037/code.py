class Solution(object):
    def solveSudoku(self, board):
        self.board = board
        self.establish()
        self.solver()

    def establish(self):
        self.possible_dict = {}
        number_set = {str(i) for i in range(1,10)}
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == '.':
                    current_set = set()  # 记录已被使用的数字集
                    # 添加当前所在行已使用的数字
                    for k in range(9):
                        value = self.board[i][k]
                        if value != '.':
                            current_set.add(value)
                    # 添加当前所在列已使用的数字        
                    for k in range(9):
                        value = self.board[k][j]
                        if value !='.':
                            current_set.add(value)
                    # 添加当前所在3*3方块已使用的数字      
                    a = (i // 3) * 3
                    b = (j // 3) * 3        
                    for k in range(9):
                        value = self.board[k//3+a][k%3+b]
                        if value !='.':
                            current_set.add(value)
                    key = (i, j)        
                    value = number_set - current_set 
                    self.possible_dict[key] = value

    def solver(self):
        if len(self.possible_dict) == 0:
            return True
        key_tuple = min(self.possible_dict.keys(), key=lambda x: len(self.possible_dict[x]))
        number_set = self.possible_dict[key_tuple]
        for number in number_set:
            update_dict = {key_tuple: self.possible_dict[key_tuple]}
            if self.is_valid(number, key_tuple, update_dict):
                if self.solver():
                    return True
            self.undo(key_tuple, update_dict) 
        return False
        
    def is_valid(self, number, key_tuple, update_dict):
        i, j = key_tuple
        a, b = i // 3, j // 3
        self.board[i][j] = number
        del self.possible_dict[key_tuple]
        for key, value in self.possible_dict.items():
            if number in value:
                key_i, key_j = key
                key_a, key_b = key_i // 3, key_j // 3
                if key_i==i or key_j==j or (key_a,key_b)==(a,b):
                    update_dict[key] = number
                    self.possible_dict[key].remove(number)
                    if len(self.possible_dict[key]) == 0:
                        return False
        return True

    def undo(self, key_tuple, update_dict):
        i, j = key_tuple
        self.board[i][j] = "."
        for key in update_dict:            
            if key not in self.possible_dict:
                self.possible_dict[key] = update_dict[key]
            else:
                self.possible_dict[key].add(update_dict[key])
        

if __name__ == '__main__':
    solution = Solution()
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    result = solution.solveSudoku(board)
    for line in board:
        print(line)
    
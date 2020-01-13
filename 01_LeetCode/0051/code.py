class Solution(object):
    def solveNQueens(self, n):
        result_list = []
        def dfs(queen_list, check1_list, check2_list):
            row = len(queen_list)
            if row == n:
                result = ['.' * k + 'Q' + '.' * (n - 1 - k) for k in queen_list]
                result_list.append(result)
                return
            for i in range(n):
                if i in queen_list or row - i in check1_list or row + i in check2_list: 
                    continue
                new_queen_list = queen_list + [i]
                new_check1_list = check1_list + [row - i]
                new_check2_list = check2_list + [row + i]
                dfs(new_queen_list, new_check1_list, new_check2_list)
        dfs([], [], [])
        return result_list
        
        
if __name__ == '__main__':
    solution = Solution()
    result = solution.solveNQueens(8)
    print(len(result))
    print(result[0])
class Solution(object):
    def combinationSum2(self, number_list, target):
        number_list.sort()
        N = len(number_list)
        result_list = self.dfs_helper(number_list, target)    
        return result_list
        
    def dfs_helper(self, number_list, target):
        if target == 0:
            return [[]]
        current_result_list = []
        i = 0
        N = len(number_list)
        while i < N:
            number = number_list[i]
            if target < number:
                break
            next_result_list = self.dfs_helper(number_list[i+1:], target-number)    
            while i+1 < N and number_list[i] == number_list[i+1]:
                i += 1
            if next_result_list != []:
                for result in next_result_list:
                    current_result_list.append([number] + result)
            i += 1        
        return current_result_list            
            

if __name__ == '__main__':
    solution = Solution()
    number_list = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    result_list = solution.combinationSum2(number_list, target)
    print(result_list)
    number_list = [2, 5, 2, 1, 2]
    target = 5
    result_list = solution.combinationSum2(number_list, target)
    print(result_list)
    
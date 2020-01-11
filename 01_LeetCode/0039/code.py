class Solution(object):
    def combinationSum(self, number_list, target):
        number_list.sort()
        N = len(number_list)
        result_list = self.dfs_helper(number_list, 0, target)    
        return result_list
        
    def dfs_helper(self, number_list, index, target):
        if target == 0:
            return [[]]
        current_result_list = []
        for i in range(index, len(number_list)):
            number = number_list[i]
            if target < number:
                break
            next_result_list = self.dfs_helper(number_list, i, target-number)    
            if next_result_list != []:
                for result in next_result_list:
                    current_result_list.append([number] + result)
        return current_result_list            
            

if __name__ == '__main__':
    solution = Solution()
    number_list = [2,3,6,7]
    target = 7
    result_list = solution.combinationSum(number_list, target)
    print(result_list)
    number_list = [2,3,5]
    target = 8
    result_list = solution.combinationSum(number_list, target)
    print(result_list)
    
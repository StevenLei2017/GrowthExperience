class Solution:
    def maxSubArray(self, number_list) -> int:
        for i in range(1, len(number_list)):
            if number_list[i-1] > 0:
                number_list[i] += number_list[i-1]
        return max(number_list)
        

if __name__ == '__main__':
    solution = Solution()
    testCase_1 = [-2,1,-3,4,-1,2,1,-5,4]
    testCase_list = [testCase_1]
    for i, testCase in enumerate(testCase_list, 1):
        result = solution.maxSubArray(testCase)
        print_result = 'Output %d: %s' %(i, result)
        print(print_result)
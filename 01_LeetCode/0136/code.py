class Solution(object):
    def singleNumber(self, number_list):
        result = 0
        for number in number_list:
            result ^= number
        return result
        

if __name__ == '__main__':
    solution = Solution()
    testCase_1 = [2,2,1]
    testCase_2 = [4,1,2,1,2]
    testCase_list = [testCase_1, testCase_2]
    for index, testCase in enumerate(testCase_list, 1):
        result = solution.singleNumber(testCase)
        print('Output %d: %d' %(index, result))
    
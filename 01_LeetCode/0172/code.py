import math


class Solution(object):
    def trailingZeroes(self, number):
        if number < 5:
            return 0 
        return sum(int(number // math.pow(5, k)) for k in range(1, int(math.log(number, 5)+1)))   
        

if __name__ == '__main__':
    solution = Solution()
    testCase_1 = 25
    testCase_2 = 5
    testCase_3 = 3
    testCase_list = [testCase_1, testCase_2, testCase_3]
    for index, testCase in enumerate(testCase_list, 1):
        result = solution.trailingZeroes(testCase)
        print('Output %d:' %index, result)
    
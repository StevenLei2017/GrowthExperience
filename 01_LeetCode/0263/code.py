class Solution(object):
    def isUgly(self, number):
        if number <= 0:
            return False
        while not number & 1:
            number >>= 1
        while number % 3 == 0:
            number //= 3
        while number % 5 == 0:
            number //= 5
        return number == 1
        
                
if __name__ == '__main__':
    solution = Solution()
    function_name = dir(solution)[-1]
    function_object = getattr(solution, function_name)
    testCase_1 = 6
    testCase_2 = 8
    testCase_3 = 14
    testCase_list = [testCase_1, testCase_2, testCase_3]
    for index, testCase in enumerate(testCase_list, 1):
        result = function_object(testCase)
        print('Output %d:' %index, result)
        
    
class Solution(object):
    def getSum(self, a, b):
        return a + b
        
        
if __name__ == '__main__':
    solution = Solution()
    function_name = dir(solution)[-1]
    function_object = getattr(solution, function_name)
    testCase_1 = [1, 2]
    testCase_2 = [-2, 3]
    testCase_list = [testCase_1, testCase_2]
    for index, testCase in enumerate(testCase_list, 1):
        result = function_object(*testCase)
        print('Output %d:' %index, result)        
        
    
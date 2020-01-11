class Solution(object):
    def intersection(self, number_list_1, number_list_2):
        return set(number_list_1).intersection(number_list_2)
        
        
if __name__ == '__main__':
    solution = Solution()
    function_name = dir(solution)[-1]
    function_object = getattr(solution, function_name)
    testCase_1 = [[1,2,2,1], [2,2]]
    testCase_2 = [[4,9,5], [9,4,9,8,4]]
    testCase_list = [testCase_1, testCase_2]
    for index, testCase in enumerate(testCase_list, 1):
        result = function_object(*testCase)
        print('Output %d:' %index, result)        
        
    
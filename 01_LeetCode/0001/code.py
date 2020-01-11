class Solution(object):
    def twoSum(self, number_list, target):
        record_dict = {}
        for index, number in enumerate(number_list):
            number_1 = target - number
            if number_1 in record_dict:
                result = [record_dict[number_1], index]
                return result
            else:
                record_dict[number] = index
        
        
if __name__ == '__main__':
    """ 主函数"""
    solution = Solution()
    function_name = dir(solution)[-1]
    function_object = getattr(solution, function_name)
    testCase_1 = [2, 7, 11, 15]
    testCase_list = [testCase_1]
    for index, testCase in enumerate(testCase_list, 1):
        result = function_object(testCase, 9)
        print('Output %d:' %index, result)
        
    
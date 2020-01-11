class Solution(object):
    def moveZeroes(self, number_list):
        length = len(number_list)
        positive_index = 0
        for index in range(length):
            if number_list[index]:
                number_list[positive_index], number_list[index] = number_list[index], number_list[positive_index]
                positive_index += 1
                
                
if __name__ == '__main__':
    solution = Solution()
    function_name = dir(solution)[-1]
    function_object = getattr(solution, function_name)
    testCase_1 = [0, 1, 0, 3, 12]
    testCase_2 = [0, 1, 0, 2, 0]
    testCase_3 = [0, 1, 0, 3, 0, 0]
    testCase_4 = [0, 0]
    testCase_list = [testCase_1, testCase_2, testCase_3,testCase_4]
    for index, testCase in enumerate(testCase_list, 1):
        result = function_object(testCase)
        print('Output %d:' %index, testCase)
        
    
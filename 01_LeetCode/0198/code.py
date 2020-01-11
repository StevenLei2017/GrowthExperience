class Solution:
    # @param n, an integer
    # @return an integer
    def rob(self, number_list):
        result = [0, 0]
        for number in number_list:
            no_rob = max(result)
            do_rob = result[0] + number
            result = [no_rob, do_rob]
        return max(result)
        

if __name__ == '__main__':
    solution = Solution()
    function_name = dir(solution)[-1]
    function_object = getattr(solution, function_name)
    testCase_1 = [1,2,3,1]
    testCase_2 = [2,7,9,3,1]
    testCase_3 = [2,1,1,2]
    testCase_list = [testCase_1, testCase_2, testCase_3]
    for index, testCase in enumerate(testCase_list, 1):
        result = function_object(testCase) 
        print('Output %d:' %index, result)
    
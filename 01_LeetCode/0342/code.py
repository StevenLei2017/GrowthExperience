class Solution(object):
    def isPowerOfFour(self, number):
        binary_string = bin(number)[2:]
        return binary_string.strip('0')=='1' and len(binary_string)%2==1
                
                
if __name__ == '__main__':
    solution = Solution()
    function_name = dir(solution)[-1]
    function_object = getattr(solution, function_name)
    testCase_1 = 16
    testCase_2 = 5
    testCase_list = [testCase_1, testCase_2]
    for index, testCase in enumerate(testCase_list, 1):
        result = function_object(testCase)
        print('Output %d:' %index, result)
        
    
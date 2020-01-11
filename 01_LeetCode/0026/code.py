class Solution:
    def removeDuplicates(self, number_list) -> int:
        if not number_list:
            return 0
        length = 1
        for i in range(1, len(number_list)):
            if number_list[i] != number_list[i-1]:
                number_list[length] = number_list[i]
                length += 1
        return length     
        

if __name__ == '__main__':
    solution = Solution()
    testCase_1 = [1,1,2]
    testCase_2 = [0,0,1,1,1,2,2,3,3,4]
    testCase_list = [testCase_1, testCase_2]
    for i, testCase in enumerate(testCase_list, 1):
        result = solution.removeDuplicates(testCase)
        print_result = 'Output %d: %s' %(i, result)
        print(print_result)
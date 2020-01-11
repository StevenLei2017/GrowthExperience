class Solution(object):
    def twoSum(self, number_list, target):
        visit_dict = {}
        for index, number in enumerate(number_list, 1):
            if number in visit_dict:
                return [visit_dict[number], index]
            else:
                visit_dict[target-number] = index
        

if __name__ == '__main__':
    solution = Solution()
    testCase_1 = [2,7,11,15]
    testCase_list = [testCase_1]
    for index, testCase in enumerate(testCase_list, 1):
        result = solution.twoSum(testCase, 9)
        print('Output %d:' %index, result)
    
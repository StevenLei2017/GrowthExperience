import math


class Solution(object):
    def majorityElement(self, number_list):
        from collections import Counter
        counter = Counter(number_list)
        return counter.most_common(1)[0][0]
        

if __name__ == '__main__':
    solution = Solution()
    testCase_1 = [3,2,3]
    testCase_2 = [2,2,1,1,1,2,2]
    testCase_3 = [10,9,9,9,10]
    testCase_list = [testCase_1, testCase_2, testCase_3]
    for index, testCase in enumerate(testCase_list, 1):
        result = solution.majorityElement(testCase)
        print('Output %d:' %index, result)
    
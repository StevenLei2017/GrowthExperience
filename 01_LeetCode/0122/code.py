class Solution(object):
    def maxProfit(self, price_list):
        result = 0
        for i in range(1, len(price_list)):
            if price_list[i] > price_list[i-1]:
                result += price_list[i] - price_list[i-1]
        return result
        

if __name__ == '__main__':
    solution = Solution()
    testCase_1 = [7, 1, 5, 3, 6, 4]
    testCase_2 = [1, 2, 3, 4, 5]
    testCase_3 = [7, 6, 4, 3, 1]
    testCase_list = [testCase_1, testCase_2, testCase_3]
    for index, testCase in enumerate(testCase_list, 1):
        result = solution.maxProfit(testCase)
        print('Output %d: %d' %(index, result))
    
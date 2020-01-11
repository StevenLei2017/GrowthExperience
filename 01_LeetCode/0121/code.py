class Solution(object):
    def maxProfit(self, price_list):
        if not price_list:
            return 0
        min_price = price_list[0]
        max_profit = 0
        for price in price_list[1:]:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(price-min_price, max_profit)
        return max_profit
        

if __name__ == '__main__':
    solution = Solution()
    testCase_1 = [7, 1, 5, 3, 6, 4]
    testCase_2 = [7, 6, 4, 3, 1]
    testCase_list = [testCase_1, testCase_2]
    for index, testCase in enumerate(testCase_list, 1):
        result = solution.maxProfit(testCase)
        print('Output %d: %d' %(index, result))
    
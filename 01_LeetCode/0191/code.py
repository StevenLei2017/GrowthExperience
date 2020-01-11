class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        result = 0
        for i in range(32):
            if n & 1:
                result += 1
            n >>= 1
        return result
        

if __name__ == '__main__':
    solution = Solution()
    testCase_1 = int('00000000000000000000000000001011', 2)
    testCase_2 = int('00000000000000000000000010000000', 2)
    testCase_3 = int('11111111111111111111111111111101', 2)
    testCase_list = [testCase_1, testCase_2, testCase_3]
    for index, testCase in enumerate(testCase_list, 1):
        result = solution.hammingWeight(testCase)
        print('Output %d:' %index, result)
    
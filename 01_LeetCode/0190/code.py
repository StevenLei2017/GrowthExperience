class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = 0
        for i in range(32):
            result = (result << 1) + (n & 1)
            n >>= 1
        return result
        

if __name__ == '__main__':
    solution = Solution()
    testCase_1 = int('00000010100101000001111010011100', 2)
    testCase_2 = int('11111111111111111111111111111101', 2)
    testCase_list = [testCase_1, testCase_2]
    for index, testCase in enumerate(testCase_list, 1):
        result = solution.reverseBits(testCase)
        print('Output %d:' %index, bin(result))
    
class Solution(object):
    def getPermutation(self, n, k):
        import math
        char_list = ['%d' %i for i in range(1, n+1)]
        result = ''
        count = n
        while count:
            divisor = math.factorial(count-1)
            quotient = (k-1) // divisor
            result += char_list.pop(quotient)
            k -= quotient * divisor
            count -= 1
        return result
        

if __name__ == '__main__':
    solution = Solution()
    result = solution.getPermutation(4, 9)
    print(result)
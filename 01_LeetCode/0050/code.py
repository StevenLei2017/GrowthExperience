class Solution(object):
    def myPow(self, x, n):
        return x ** n
        

if __name__ == '__main__':
    solution = Solution()
    x, n = 2.0, 10
    result = solution.myPow(x, n)
    print('%.5f' %result)
    x, n = 2.1, 3
    result = solution.myPow(x, n)
    print('%.5f' %result)
    x, n = 2.0, -2
    result = solution.myPow(x, n)
    print('%.5f' %result)
    
    
class Solution(object):
    def reverse(self, x):
        x_string = str(x)
        if x_string[0] == '-':
            reversed_x_string = '-' + x_string[:0:-1]
        else:
            reversed_x_string = x_string[::-1]
        reversed_x = int(reversed_x_string)    
        if reversed_x < -(2**31) or reversed_x > 2**31-1:
            reversed_x = 0
        return reversed_x

                    
if __name__ == '__main__':
    solution = Solution()
    x = 123
    result = solution.reverse(x)
    print(result)
    x = -123
    result = solution.reverse(x)
    print(result)
    x = 120
    result = solution.reverse(x)
    print(result)
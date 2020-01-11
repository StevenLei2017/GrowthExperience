class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        x_string = str(x)
        if x_string[::-1] == x_string:
            return True
        else:
            return False

                    
if __name__ == '__main__':
    solution = Solution()
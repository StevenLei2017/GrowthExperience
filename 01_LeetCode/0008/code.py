class Solution(object):
    def myAtoi(self, s):
        s = s.lstrip()
        if not s:
            return 0
        if s[0].isdigit() or s[0]=='+' or s[0]=='-':
            i = 1
            while i < len(s):
                if not s[i].isdigit():
                    break
                i += 1
            s = s[:i]
            try:
                result = int(s)
            except Exception:
                result = 0
            if result < -2**31:
                result = -2**31
            elif result > 2**31-1:
                result = 2**31-1
            return result    
        else:
            return 0

                    
if __name__ == '__main__':
    solution = Solution()
    x = '42'
    result = solution.myAtoi(x)
    print(result)
    x = '  -42'
    result = solution.myAtoi(x)
    print(result)
    x = '4193 with words'
    result = solution.myAtoi(x)
    print(result)
    x = 'words and 987'
    result = solution.myAtoi(x)
    print(result)
    x = '-91283472332'
    result = solution.myAtoi(x)
    print(result)
    x = '3.14159'
    result = solution.myAtoi(x)
    print(result)
    x = '+'
    result = solution.myAtoi(x)
    print(result)
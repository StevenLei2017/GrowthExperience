class Solution(object):
    def isMatch(self, s, p):
        # table[i][j] means the match status between pattern[:i] and string[:j]
        # table[0][0] means the match status of two empty strings
        # table[1][1] means the match status of p[0] and s[0]
        table = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
        table[0][0] = True
        # s为空的情况
        for i in range(2, len(p) + 1):
            table[i][0] = table[i - 2][0] and p[i - 1] == '*'
        # 固定patter,遍历string    
        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                if p[i - 1] != "*":  # 当pattern字符不为*时
                    table[i][j] = table[i - 1][j - 1] and \
                        (p[i - 1] == s[j - 1] or p[i - 1] == '.')
                else:  # 当pattern字符为*时
                    table[i][j] = table[i - 2][j] or table[i - 1][j]    
                    if p[i - 2] == s[j - 1] or p[i - 2] == '.':
                        table[i][j] |= table[i][j - 1]
        return table[-1][-1]

                    
if __name__ == '__main__':
    solution = Solution()
    string = "aaa"
    pattern = "ab*a*c*a"
    result = solution.isMatch(string, pattern)
    print(result)
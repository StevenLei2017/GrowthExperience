class Solution(object):
    def isMatch(self, s, p):
        l = len(s)
        if len(p) - p.count('*') > l:
            return False
        dp = [True]  + [False] * l
        for letter in p:
            new_dp = [dp[0] and letter == '*']
            if letter == '*':
                for j in range(l):
                    new_dp.append(new_dp[-1] or dp[j + 1])
            elif letter == '?':
                new_dp += dp[:l]
            else:
                new_dp += [dp[j] and s[j] == letter for j in range(l)]
            dp = new_dp
        return dp[-1]
        

if __name__ == '__main__':
    solution = Solution()
    number1_string = '123'
    number2_string = '456'
    result = solution.multiply(number1_string, number2_string)
    print(result)
    
class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.rstrip(' ')
        N = len(s)
        i = N - 1
        while i >= 0:
            if s[i] !=  ' ':
                i -= 1
            else:
                break
        last_word = s[i+1:N]        
        result = len(last_word)
        return result


if __name__ == '__main__':
    solution = Solution()
    testCase = '  a '
    result = solution.lengthOfLastWord(testCase)
    print(result)
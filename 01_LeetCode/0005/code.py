class Solution(object):
    def longestPalindrome(self, string):
        self.string = string
        self.length = len(string)
        result = ''
        for i in range(self.length):
            # 回文子字符串长度为奇数
            palindrome_substring = self.inner_to_outer(i, i)
            if len(palindrome_substring) > len(result):
                result = palindrome_substring
            # 回文子字符串长度为偶数
            palindrome_substring = self.inner_to_outer(i, i+1)
            if len(palindrome_substring) > len(result):
                result = palindrome_substring
        return result    

    def inner_to_outer(self, left, right):
        while left>=0 and right<self.length and self.string[left]==self.string[right]:
            left -= 1
            right += 1
        palindrome_substring = self.string[left+1:right]     
        return palindrome_substring   

                    
if __name__ == '__main__':
    solution = Solution()
    testCase_1 = "babad"
    testCase_2 = "cbbd"
    testCase_list = [testCase_1, testCase_2]
    for index, testCase in enumerate(testCase_list, 1):
        result = solution.longestPalindrome(testCase)
        print('Output %d:' %index, result)
        
    
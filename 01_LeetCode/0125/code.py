import string


class Solution(object):
    def isPalindrome(self, test_string):
        punctuation = string.punctuation + ' '
        trans = str.maketrans('', '', punctuation)
        test_string = test_string.translate(trans).lower()
        reversed_string = test_string[::-1]
        return test_string == reversed_string
            

if __name__ == '__main__':
    solution = Solution()
    testCase_1 = "A man, a plan, a canal: Panama"
    testCase_2 = "race a car"
    testCase_3 = "noon"
    testCase_4 = "abaa"
    testCase_list = [testCase_1, testCase_2, testCase_3, testCase_4]
    for index, testCase in enumerate(testCase_list, 1):
        result = solution.isPalindrome(testCase)
        print('Output %d: %d' %(index, result))
    
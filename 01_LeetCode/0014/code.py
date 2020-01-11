class Solution(object):
    def longestCommonPrefix(self, string_list):
        i = 0
        length_list = [len(k) for k in string_list]
        min_length = min(length_list)
        first_string = string_list[0]
        while i < min_length:
            char = first_string[i]
            is_same = True
            for string in string_list[1:]:
                if char != string[i]:
                    is_same = False
                    break
            if not is_same:
                break
            i += 1    
        result = first_string[:i]    
        return result 
                    
                    
if __name__ == '__main__':
    solution = Solution()
    testCase_1 = ["flower","flow","flight"]
    testCase_list = [testCase_1]
    for i, testCase in enumerate(testCase_list):
        result = solution.longestCommonPrefix(testCase)
        print('Output %d:' %i, result)
    
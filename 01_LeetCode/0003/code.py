class Solution(object):
    def lengthOfLongestSubstring(self, string):
        record_dict, result, start = {}, 0, 0
        for index, char in enumerate(string):
            if char in record_dict:
                result = max(result, index-start)
                start = max(start, record_dict[char]+1)
            record_dict[char] = index
        result = max(result, len(string)-start)
        return result
                
                
if __name__ == '__main__':
    solution = Solution()
    testCase_1 = "hdgikkinyyzxycsekxoev"
    testCase_2 = "bbbbb"
    testCase_3 = "pwwkew"
    testCase_4 = "aab"
    testCase_list = [testCase_1, testCase_2, testCase_3, testCase_4]
    for index, testCase in enumerate(testCase_list, 1):
        result = solution.lengthOfLongestSubstring(testCase)
        print('Output %d:' %index, result)
        
    
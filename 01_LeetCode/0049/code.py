class Solution(object):
    def groupAnagrams(self, string_list):
        record_dict = {}
        for string in string_list:
            sorted_string = ''.join(sorted(string))
            if sorted_string in record_dict:
                record_dict[sorted_string].append(string)
            else:
                record_dict[sorted_string] = [string]
        result_list = list(record_dict.values())
        return result_list
        

if __name__ == '__main__':
    solution = Solution()
    testCase = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = solution.groupAnagrams(testCase)
    print(result)
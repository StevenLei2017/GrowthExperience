class Solution(object):
    def romanToInt(self, input_string):
        roman2value_dict = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1}
        s = input_string
        result = 0
        while s:
            if s[:2] in roman2value_dict:
                result += roman2value_dict[s[:2]]
                s = s[2:]
            else:
                result += roman2value_dict[s[0]] 
                s = s[1:]
        return result        
                
                    
if __name__ == '__main__':
    solution = Solution()
    testCase_1 = 'IV'    
    testCase_2 = 'IX'
    testCase_3 = 'LVIII'
    testCase_4 = 'MCMXCIV'
    testCase_list = [testCase_1, testCase_2, testCase_3, testCase_4]
    for i, testCase in enumerate(testCase_list):
        result = solution.romanToInt(testCase)
        print('Output %d:' %i, result)
    
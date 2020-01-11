class Solution(object):
    def letterCombinations(self, digit_list):
        if not digit_list:
            return []
        digit2letter_dict = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'}
        combination_list = list(digit2letter_dict[digit_list[0]])    
        for digit in digit_list[1:]:
            letter_list = list(digit2letter_dict[digit])
            temp_list = []
            for combination in combination_list:
                temp_list.extend([combination+k for k in letter_list])
            combination_list = temp_list
        return combination_list    
    
                    
if __name__ == '__main__':
    solution = Solution()
    testCase = '23'
    combination_list = solution.letterCombinations(testCase)
    print(combination_list)
    
        
    
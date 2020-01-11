class Solution:
    def isValid(self, input_string):
        map_dict = {
            '{': '}',
            '(': ')',
            '[': ']'}
        stack = []
        for every_char in input_string:
            if every_char in map_dict.keys():
                stack.append(map_dict[every_char])
            else:
                if len(stack) == 0:
                    return False
                else:    
                    pop_char = stack.pop()
                    if pop_char != every_char:
                        return False
        if len(stack) != 0:
            return False
        else:
            return True
        

if __name__ == '__main__':
    solution = Solution()
    testCase_1 = '()'
    testCase_2 = '()[]{}'
    testCase_3 = '(]'
    testCase_4 = '([)]'
    testCase_5 = '{[]}'
    testCase_list = [testCase_1, testCase_2, testCase_3, testCase_4, testCase_5]
    for i, testCase in enumerate(testCase_list, 1):
        result = solution.isValid(testCase)
        print_result = 'Output %d: %s' %(i, result)
        print(print_result)
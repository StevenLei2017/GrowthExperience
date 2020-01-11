class Solution(object):
    def generateParenthesis(self, n):       
        result_list = []
        def helper(left, right, left_unmatched, path):
            """
            variable meaning:
            left: number of '(' not used
            right: number of ')' not used
            left: number of '(' not matched in path
            """
            if right == 0:
                result_list.append(path)
            elif left == 0:
                path += ')'
                right -= 1
                left_unmatched -= 1
                helper(left, right, left_unmatched, path)
            elif left_unmatched == 0:
                path += '('
                left -= 1
                left_unmatched += 1
                helper(left, right, left_unmatched, path)
            else:
                # way 1: add ( to path, and continue
                path_1 = path + '('
                left_1 = left - 1
                left_unmatched_1 = left_unmatched + 1
                helper(left_1, right, left_unmatched_1, path_1)
                # way 2: add ) to path, and continue
                path_2 = path + ')'
                right_2 = right - 1
                left_unmatched_2 = left_unmatched - 1
                helper(left, right_2, left_unmatched_2, path_2)
        helper(n, n, 0, '')        
        return result_list
                
                
if __name__ == '__main__':
    solution = Solution()
    testCase_1 = 2
    testCase_2 = 3
    testCase_list = [testCase_1, testCase_2]
    for i, testCase in enumerate(testCase_list, 1):
        result = solution.generateParenthesis(testCase)
        print_result = 'Output %d: %s' %(i, result)
        print(print_result)
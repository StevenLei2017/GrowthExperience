class Solution:
    def merge(self, number_list_1, m, number_list_2, n):
        while m > 0 and n > 0:
            if number_list_1[m-1] > number_list_2[n-1]:
                number_list_1[m+n-1] = number_list_1[m-1]
                m -= 1
            elif number_list_1[m-1] <= number_list_2[n-1]:
                number_list_1[m+n-1] = number_list_2[n-1]
                n -= 1
        if n > 0:
            number_list_1[:n] = number_list_2[:n]
        

if __name__ == '__main__':
    solution = Solution()
    testCase_1 = [[1, 2, 3, 0, 0, 0], [2, 5, 6]]
    testCase_list = [testCase_1]
    for i, testCase in enumerate(testCase_list, 1):
        solution.merge(testCase[0], 3, testCase[1], len(testCase[1]))
        print_result = 'Output %d: %s' %(i, testCase[0])
        print(print_result)
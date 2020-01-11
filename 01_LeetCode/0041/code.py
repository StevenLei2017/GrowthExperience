class Solution(object):
    def firstMissingPositive(self, number_list):
        N = len(number_list)
        for i, number in enumerate(number_list):
            if number <= 0:
                number_list[i] = float('inf')
        for number in number_list:
            absolute_number = abs(number)
            if absolute_number <= N and number_list[absolute_number-1] > 0:
                number_list[absolute_number-1] *= -1
        for i, number in enumerate(number_list):
            if number > 0:
                return i + 1
        return N + 1
        

if __name__ == '__main__':
    solution = Solution()
    number_list = [3, 4, -1, 1]
    result = solution.firstMissingPositive(number_list)
    print(result)
    number_list = [7, 8, 9, 11, 12]
    result = solution.firstMissingPositive(number_list)
    print(result)
    
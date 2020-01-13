class Solution(object):
    def permute(self, number_list):
        result_list = [[]]
        for index, number in enumerate(number_list, 1):
            temp_list = []
            for result in result_list:
                for i in range(index):
                    temp_list.append(result[:i] + [number] + result[i:])
            result_list = temp_list
        return result_list
        

if __name__ == '__main__':
    solution = Solution()
    testCase = [1, 2, 3]
    result = solution.permute(testCase)
    print(result)
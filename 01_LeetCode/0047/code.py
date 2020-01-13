class Solution(object):
    def permuteUnique(self, number_list):
        result_list = [[]]
        for index, number in enumerate(number_list, 1):
            temp_list = []
            for result in result_list:
                for i in range(index):
                    temp = result[:i] + [number] + result[i:]
                    temp_list.append(temp)
                    # handles duplication
                    if i < len(result) and result[i] == number:
                        break              
            result_list = temp_list
        return result_list
        

if __name__ == '__main__':
    solution = Solution()
    testCase = [1, 1, 3, 3]
    result = solution.permuteUnique(testCase)
    print(result)
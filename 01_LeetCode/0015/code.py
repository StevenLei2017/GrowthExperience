class Solution(object):
    def threeSum(self, number_list):
        """ """
        if len(number_list) < 3:
            return []    
        result_list = []
        number_list.sort()
        length = len(number_list)
        for i in range(len(number_list)-2):
            if number_list[i] > 0:
                break
            if i > 0 and number_list[i] == number_list[i-1] :
                continue
            left_index, right_index = i+1, length-1
            while left_index < right_index:
                s = number_list[i] + number_list[left_index] + number_list[right_index]
                if s < 0:
                    left_index += 1
                elif s > 0:
                    right_index -= 1
                else:
                    result_list.append([number_list[i], number_list[left_index], number_list[right_index]])
                    left_index += 1
                    right_index -= 1
                    while left_index < right_index and number_list[left_index] == number_list[left_index-1]:    
                        left_index += 1
                    while left_index < right_index and number_list[right_index] == number_list[right_index+1]:
                        right_index -= 1
        return result_list    
    
                    
if __name__ == '__main__':
    solution = Solution()
    testCase_1 = [-1, 0, 1, 2, -1, -4]
    testCase_list = [testCase_1]
    for index, testCase in enumerate(testCase_list, 1):
        result = solution.threeSum(testCase)
        print('Output %d:' %index, result)
        
    
class Solution(object):
    def searchRange(self, number_list, target):
        if not number_list or target < number_list[0]:
            return [-1, -1]
        N = len(number_list)    
        left_index, right_index = 0, N-1
        while left_index <= right_index:
            middle_index = (left_index + right_index) // 2
            middle_value = number_list[middle_index]
            if middle_value < target:
                left_index = middle_index + 1
            elif middle_value > target:
                right_index = middle_index - 1
            else:
                for index in range(left_index, middle_index+1):
                    if number_list[index] == target:
                        left_result = index
                        break
                for index in range(right_index, middle_index-1, -1):
                    if number_list[index] == target:
                        right_result = index
                        break
                result_list = [left_result, right_result]
                return result_list
        return [-1, -1]        


if __name__ == '__main__':
    solution = Solution()
    number_list = [0,0,0,0,1,2,3,3,4,5,6,6,7,8,8,8,9,9,10,10,11,11]
    target = 0
    result = solution.searchRange(number_list, target)
    print(result)
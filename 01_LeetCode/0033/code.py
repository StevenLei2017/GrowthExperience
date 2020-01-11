class Solution(object):
    def search(self, number_list, target):
        N = len(number_list)
        left_index, right_index = 0, N-1
        while left_index <= right_index:
            middle_index = (left_index + right_index) // 2
            middle_value = number_list[middle_index]
            left_value = number_list[left_index]
            right_value = number_list[right_index]
            if middle_value == target:
                return middle_index
            if left_value <= middle_value:
                if left_value <= target <= middle_value:
                    right_index = middle_index - 1
                else:
                    left_index = middle_index + 1
            else:
                if middle_value <= target <= right_value:
                    left_index = middle_index + 1
                else:
                    right_index = middle_index - 1
        return -1
            

if __name__ == '__main__':
    solution = Solution()
    number_list = [3, 5, 1]
    target = 3
    result = solution.search(number_list, target)
    print(result)
class Solution(object):
    def searchInsert(self, number_list, target):
        if target > number_list[-1]:
            return len(number_list)
        for i, number in enumerate(number_list):
            if number >= target:
                return i
        

if __name__ == '__main__':
    solution = Solution()
    result = solution.searchInsert([1,3,5,6], 5)
    print(result)
    result = solution.searchInsert([1,3,5,6], 2)
    print(result)
    result = solution.searchInsert([1,3,5,6], 7)
    print(result)
    result = solution.searchInsert([1,3,5,6], 0)
    print(result)
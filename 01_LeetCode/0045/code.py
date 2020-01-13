class Solution(object):
    def jump(self, nums):
        result = 0
        current_jump_max = 0
        previous_jump_max = 0
        for i in range(len(nums) - 1):
            current_jump_max = max(current_jump_max, i + nums[i])
            if i == previous_jump_max:
                result += 1 
                previous_jump_max = current_jump_max
        return result
        

if __name__ == '__main__':
    solution = Solution()
    testCase = [2, 3, 1, 1, 4]
    result = solution.jump(testCase)
    print(result)
    
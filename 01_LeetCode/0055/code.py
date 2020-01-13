class Solution(object):
    def canJump(self, number_list):
        if len(number_list) == 1:
            return True
        max_reach, N = 0, len(number_list)
        for i, number in enumerate(number_list):
            if max_reach >= N-1:
                return True
            if max_reach < i:
                return False
            max_reach = max(max_reach, i+number)
              

if __name__ == '__main__':
    solution = Solution()
    testCase_1 = [2, 3, 1, 1, 4]
    result = solution.canJump(testCase_1)
    print(result)
    testCase_2 = [2, 0, 0]
    result = solution.canJump(testCase_2)
    print(result)
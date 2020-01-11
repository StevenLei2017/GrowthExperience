class Solution(object):
    def trap(self, height_list):
        if not height_list:
            return 0
        max_left, max_right = 0, 0
        result = 0
        max_value = max(height_list)
        max_index = height_list.index(max_value)
        # 累加最高柱子左边的雨水体积
        for height in height_list[:max_index]:
            max_left = max(max_left, height)
            result += (max_left - height)
		# 累加最高柱子右边的雨水体积	
        for height in height_list[-1:max_index:-1]:
            max_right = max(max_right, height)
            result += (max_right - height)
        return result
        

if __name__ == '__main__':
    solution = Solution()
    height_list = [0,1,0,2,1,0,1,3,2,1,2,1]
    result = solution.trap(height_list)
    print(result)
    
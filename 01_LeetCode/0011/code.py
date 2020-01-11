class Solution(object):
    def maxArea(self, height_list):
        length = len(height_list)
        left_index = 0
        right_index = length - 1
        max_area = 0
        while left_index < right_index:
            left_height = height_list[left_index]
            right_height = height_list[right_index]
            if left_height < right_height:
                current_area = (right_index - left_index) * left_height 
                while height_list[left_index]<=left_height and left_index<length:
                    left_index += 1
            else:
                current_area = (right_index - left_index) * right_height 
                while height_list[right_index]<=right_height and right_index>0:
                    right_index -= 1
            max_area = max(max_area, current_area)        
        return max_area        
            
                    
if __name__ == '__main__':
    solution = Solution()
    testCase_1 = [1,8,6,2,5,4,8,3,7]
    testCase_list = [testCase_1]
    for index, testCase in enumerate(testCase_list, 1):
        result = solution.maxArea(testCase)
        print('Output %d:' %index, result)
        
    
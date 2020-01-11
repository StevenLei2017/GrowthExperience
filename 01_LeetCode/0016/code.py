class Solution(object):
    def threeSumClosest(self, number_list, target):
        """ """
        if len(number_list) < 3:
            return []    
        number_list.sort()
        length = len(number_list)
        threeSum_list = []
        for i in range(length-2):
            left_index, right_index = i+1, length-1
            if number_list[i] + number_list[left_index] + number_list[left_index+1] > target:
                threeSum = number_list[i] + number_list[left_index] + number_list[left_index+1]
                threeSum_list.append(threeSum)
            elif number_list[i] + number_list[right_index] + number_list[right_index-1] < target:
                threeSum = number_list[i] + number_list[right_index] + number_list[right_index-1]
                threeSum_list.append(threeSum)
            else:       
                while left_index < right_index:
                    threeSum = number_list[i] + number_list[left_index] + number_list[right_index]
                    threeSum_list.append(threeSum)
                    if threeSum < target:
                        left_index += 1
                    elif threeSum > target:
                        right_index -= 1
                    else:
                        return threeSum
        threeSum_list.sort(key = lambda x: abs(x-target))
        threeSum = threeSum_list[0]
        return threeSum
    
                    
if __name__ == '__main__':
    solution = Solution()
    testCase_1 = [1,2,4,8,16,32,64,128]
    testCase_list = [testCase_1]
    for index, testCase in enumerate(testCase_list, 1):
        result = solution.threeSumClosest(testCase, 82)
        print('Output %d:' %index, result)
        
    
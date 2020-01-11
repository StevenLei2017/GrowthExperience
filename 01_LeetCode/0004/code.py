class Solution(object):
    def findMedianSortedArrays(self, number_list_1, number_list_2):
        length_1 = len(number_list_1)
        length_2 = len(number_list_2)
        if (length_1 + length_2) % 2 == 1:
            k = (length_1 + length_2 + 1) // 2
            result = self.findKth(number_list_1, number_list_2, k)
        else:
            k = (length_1 + length_2) // 2
            result = self.findKth(number_list_1, number_list_2, k, is_average=True)
        return result    
        
    def findKth(self, number_list_1, number_list_2, k, is_average=False):
        # print(number_list_1, number_list_2, k, is_average)
        length_1 = len(number_list_1)
        length_2 = len(number_list_2)
        if length_1 > length_2:
            return self.findKth(number_list_2, number_list_1, k, is_average)
        if length_1 == 0:
            if not is_average:
                result = number_list_2[k-1]
            else:
                result = (number_list_2[k-1] + number_list_2[k]) / 2
            return result    
        if k == 1:
            if not is_average: # 求第K个数
                result = min(number_list_1[0], number_list_2[0])
                return result
            else: # 求第K个数和第K+1个数的平均值
                if number_list_1[0] < number_list_2[0]:
                    number_k = number_list_1[0]
                    number_k1 = self.findKth(number_list_1[1:], number_list_2, 1)
                    result = (number_k + number_k1) / 2
                    return result
                else:
                    number_k = number_list_2[0]
                    number_k1 = self.findKth(number_list_2[1:], number_list_1, 1)
                    result = (number_k + number_k1) / 2
                    return result
        half_k = k >> 1
        if length_1 <= half_k:
            index_1 = length_1
        else:
            index_1 = half_k
        index_2 = half_k
        if number_list_1[index_1-1] < number_list_2[index_2-1]:
            k = k - index_1
            return self.findKth(number_list_1[index_1:], number_list_2, k, is_average)
        else:
            k = k - index_2
            return self.findKth(number_list_1, number_list_2[index_2:], k, is_average)
        
        
if __name__ == '__main__':
    """ 主函数"""
    solution = Solution()
    number_list_1 = []
    number_list_2 = [2, 3]
    result = solution.findMedianSortedArrays(number_list_1, number_list_2)
    print(result)
    number_list_1 = [1, 2]
    number_list_2 = [3, 4]
    result = solution.findMedianSortedArrays(number_list_1, number_list_2)
    print(result)
    
    
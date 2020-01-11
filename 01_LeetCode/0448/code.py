class Solution(object):
    def findDisappearedNumbers(self, number_list):
        for i in range(len(number_list)):
            number = number_list[i]
            if number:
                index = number - 1
                while number_list[index]:
                    number_list[index], index = 0, number_list[index]-1
        index_list = []
        for index, number in enumerate(number_list, 1):
            if number:
                index_list.append(index)
        return index_list
            
       
if __name__ == '__main__':
    """ 主函数"""
    solution = Solution()
    testCase = [4,3,2,7,7,2,3,1]
    result = solution.findDisappearedNumbers(testCase)
    print('result:', result)
    
    
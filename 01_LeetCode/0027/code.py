class Solution:
    def removeElement(self, number_list, val):
        length = len(number_list)
        i = 0
        remove_count = 0
        while i + remove_count < length:
            if number_list[i] == val:
                number_list.pop(i)
                remove_count += 1
            else:
                i += 1
        result = len(number_list)
        return result
        

if __name__ == '__main__':
    solution = Solution()
    testCase_1 = [0,1,2,2,3,0,4,2]
    result = solution.removeElement(testCase_1, 2)
    print(result)
    print(testCase_1)
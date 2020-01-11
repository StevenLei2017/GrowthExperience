class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
        
class Solution(object):
    def containsNearbyDuplicate(self, number_list, k):
        """ :rtype: bool"""
        counter_dict = {}
        for index, number in enumerate(number_list):
            if number in counter_dict and index - counter_dict[number] <= k:
                return True
            counter_dict[number] = index    
        return False        
             
        
if __name__ == '__main__':
    solution = Solution()
    function_name = dir(solution)[-1]
    function_object = getattr(solution, function_name)
    testCase_1 = [[1,2,3,1], 3]
    testCase_2 = [[1,0,1,1], 1]
    testCase_3 = [[1,2,3,1,2,3], 2]
    testCase_list = [testCase_1, testCase_2, testCase_3]
    for index, testCase in enumerate(testCase_list, 1):
        result = function_object(*testCase)
        print('Output %d:' %index, result) 
    
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        

class Solution(object):
    def addTwoNumbers(self, head_1, head_2):
        number_1 = self.listNode_to_number(head_1)
        number_2 = self.listNode_to_number(head_2)
        number_3 = number_1 + number_2
        head_3 = self.number_to_listNode(number_3)
        return head_3
        
    def listNode_to_number(self, listNode):
        number_string = ''
        while listNode:
            number_string = str(listNode.val) + number_string
            listNode = listNode.next
        number = int(number_string)
        return number
        
    def number_to_listNode(self, number):
        number_string = str(number)[::-1]
        listNode = self.get_listNode(number_string)
        return listNode
        
    def get_listNode(self, number_string):   
        length = len(number_string)
        first_digit = int(number_string[0])
        head_listNode = ListNode(first_digit)
        pointer = head_listNode
        for i in range(1, length):
            digit = int(number_string[i])
            listNode = ListNode(digit)
            pointer.next = listNode
            pointer = listNode
        return head_listNode
        
        
if __name__ == '__main__':
    """ 主函数"""
    solution = Solution()
    function_name = dir(solution)[-1]
    function_object = getattr(solution, function_name)
    testCase_1 = [solution.number_to_listNode(342), 
        solution.number_to_listNode(465)]
    testCase_list = [testCase_1]
    for index, testCase in enumerate(testCase_list, 1):
        result = solution.addTwoNumbers(*testCase)
        print('Output %d:' %index, solution.listNode_to_number(result))
        
    
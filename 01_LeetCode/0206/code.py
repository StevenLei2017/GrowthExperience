class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
        
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        pointer_1 = None
        pointer_2 = head
        while pointer_2:
            next_listNonde = pointer_2.next
            pointer_2.next = pointer_1
            pointer_1 = pointer_2
            pointer_2 = next_listNonde
        return pointer_1
        
                
def show_result(head_listNode):
    while head_listNode:
        print(head_listNode.val, end=' ')
        head_listNode = head_listNode.next
    print()    
                
if __name__ == '__main__':
    solution = Solution()
    function_name = dir(solution)[-1]
    function_object = getattr(solution, function_name)
    listNode_1 = ListNode(1)
    listNode_2 = ListNode(2)
    listNode_3 = ListNode(3)
    listNode_4 = ListNode(4)
    listNode_5 = ListNode(5)
    listNode_6 = ListNode(6)
    listNode_1.next = listNode_2
    listNode_2.next = listNode_3
    listNode_3.next = listNode_4
    listNode_4.next = listNode_5
    listNode_5.next = listNode_6
    testCase_1 = listNode_1
    testCase_list = [testCase_1]
    for index, testCase in enumerate(testCase_list, 1):
        show_result(testCase)
        result = function_object(testCase)
        show_result(result) 
        
    
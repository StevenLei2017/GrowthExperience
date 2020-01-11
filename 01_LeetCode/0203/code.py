class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
        
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # 解决头节点开始有一段节点的值为val的情况
        # 本题共3个难点, 剩余的2个难点：连续节点为val, 结束节点为val
        if not head:
            return head
        while head.val == val:
            head = head.next
            if not head:
                return head
        pointer_1 = head
        pointer_2 = head.next
        while pointer_2:
            # 指针2的值为val
            if pointer_2.val == val:
                pointer_2 = pointer_2.next
            else:
                pointer_1.next = pointer_2
                pointer_1 = pointer_2
                pointer_2 = pointer_1.next
        pointer_1.next = pointer_2        
        return head
        
                
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
    listNode_2 = ListNode(6)
    listNode_3 = ListNode(6)
    listNode_4 = ListNode(3)
    listNode_5 = ListNode(6)
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
        result = function_object(testCase, 6)
        show_result(result) 
        
    
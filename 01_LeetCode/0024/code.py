class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        if not head:
            return 
        if not head.next:
            return head
        pointer_0 = None    
        pointer_1 = head
        head = head.next
        pointer_2 = pointer_1.next
        while pointer_1 and pointer_2:
            if pointer_0:
                pointer_0.next = pointer_2
            pointer_1.next = pointer_2.next
            pointer_2.next = pointer_1
            pointer_0 = pointer_1
            if pointer_1.next:
                pointer_1 = pointer_1.next
            else:
                break
            if pointer_1.next:
                pointer_2 = pointer_1.next
            else:
                break
        return head    
            

if __name__ == '__main__':
    solution = Solution()
    listNode_1 = ListNode(1)
    listNode_2 = ListNode(2)
    listNode_3 = ListNode(3)
    listNode_4 = ListNode(4)
    listNode_5 = ListNode(5)
    listNode_1.next = listNode_2
    listNode_2.next = listNode_3
    listNode_3.next = listNode_4
    listNode_4.next = listNode_5
    head = listNode_1
    pointer = solution.swapPairs(head)
    while pointer:
        print(pointer.val)
        pointer = pointer.next
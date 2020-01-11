class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        fast = slow = head
        for i in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next 
            slow = slow.next
        slow.next = slow.next.next
        return head
        
                    
if __name__ == '__main__':
    solution = Solution()
    head_listNode = ListNode(1)
    head_listNode.next = ListNode(2)
    head_listNode.next.next = ListNode(3)
    solution.removeNthFromEnd(head_listNode, 2)
    pointer = head_listNode
    while pointer:
        print(pointer.val)
        pointer = pointer.next
        
    
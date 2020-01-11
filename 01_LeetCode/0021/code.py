class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

 
class Solution(object):
    def mergeTwoLists(self, head_1, head_2):
        pointer_1 = head_1
        pointer_2 = head_2
        new_head = ListNode(0)
        pointer_3 = new_head
        while pointer_1 and pointer_2:
            if pointer_1.val < pointer_2.val:
                pointer_3.next = pointer_1
                pointer_1 = pointer_1.next
            else:
                pointer_3.next = pointer_2
                pointer_2 = pointer_2.next
            pointer_3 = pointer_3.next
        if pointer_1:
            pointer_3.next = pointer_1
        else:
            pointer_3.next = pointer_2
        return new_head.next
                
 
if __name__ == '__main__':
    solution = Solution()
    
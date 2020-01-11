class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        pointer = head
        listNode_list = []
        length = self.get_length(head)
        if length < k:
            return head
        i = 0
        N_group = length // k
        pre = None
        while i < N_group:
            for j in range(k):
                listNode_list.append(pointer)
                pointer = pointer.next
            if i == 0:
                head = listNode_list[-1]       
            for j in range(1, k):            
                listNode_list[j].next = listNode_list[j-1]
            listNode_list[0].next = pointer
            if pre:
                pre.next = listNode_list[-1]
            pre = listNode_list[0]
            listNode_list.clear()    
            i += 1
        return head
        
    def get_length(self, head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length
            

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
    pointer = solution.reverseKGroup(head, 2)
    while pointer:
        print(pointer.val)
        pointer = pointer.next
class Solution(object):
    def mergeKLists(self, head_list):
        listNode_list, new_head = [], ListNode(0)
        pointer = new_head
        for head in head_list:
            while head:
                listNode_list.append(head)
                head = head.next
        for listNode in sorted(listNode_list, key = lambda x: x.val):
            pointer.next = listNode
            pointer = pointer.next
        result = new_head.next   
        return result
                

if __name__ == '__main__':
    solution = Solution()
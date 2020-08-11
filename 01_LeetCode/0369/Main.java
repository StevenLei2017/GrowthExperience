class ListNode {
    int val;
    ListNode next;

    ListNode(int value) {
        this.val = value;
    }
}

class Solution {

    public ListNode plusOne(ListNode head) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode i = dummy, j = dummy;
        while (j.next != null) {
            j = j.next;
            if (j.val != 9) {
                i = j;
            }
        }
        i.val += 1;
        i = i.next;
        while (i != null) {
            i.val = 0;
            i = i.next;
        }
        if (dummy.val == 1) {
            return dummy;
        }
        return dummy.next;
    }

}

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        ListNode listNode1 = new ListNode(9);
        ListNode listNode2 = new ListNode(9);
        listNode1.next = listNode2;
        ListNode result = solution.plusOne(listNode1);
        while (result != null) {
            System.out.println(result.val);
            result = result.next;
        }
    }

}

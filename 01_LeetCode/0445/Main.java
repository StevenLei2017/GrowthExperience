import java.util.Stack;

class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        this.val = x;
    }
}

class Solution {

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        Stack<Integer> stack1 = new Stack<>();
        Stack<Integer> stack2 = new Stack<>();
        while (l1 != null) {
            stack1.push(l1.val);
            l1 = l1.next;
        }
        while (l2 != null) {
            stack2.push(l2.val);
            l2 = l2.next;
        }
        ListNode current = new ListNode(0);
        int sum = 0;
        while (!stack1.isEmpty() || !stack2.isEmpty()) {
            if (!stack1.isEmpty()) {
                sum += stack1.pop();
            }
            if (!stack2.isEmpty()) {
                sum += stack2.pop();
            }
            current.val = sum % 10;
            ListNode head = new ListNode(sum / 10);
            head.next = current;
            current = head;
            sum /= 10;
        }
        return current.val == 0 ? current.next : current;
    }

}

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        ListNode l17 = new ListNode(7);
        ListNode l12 = new ListNode(2);
        ListNode l14 = new ListNode(4);
        ListNode l13 = new ListNode(3);
        l17.next = l12;
        l12.next = l14;
        l14.next = l13;
        ListNode l25 = new ListNode(5);
        ListNode l26 = new ListNode(6);
        ListNode l24 = new ListNode(4);
        l25.next = l26;
        l26.next = l24;
        ListNode result = solution.addTwoNumbers(l17, l25);
        while (result != null) {
            System.out.println(result.val);
            result = result.next;
        }
    }

}

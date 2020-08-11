import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

class Node {
    public int val;
    public List<Node> children;

    public Node() {
    }

    public Node(int _val) {
        this.val = _val;
    }

    public Node(int _val, List<Node> _children) {
        this.val = _val;
        this.children = _children;
    }
};

class Solution {
    public List<Integer> preorder(Node root) {
        List<Integer> result = new ArrayList<>();
        if (root == null) {
            return result;
        }
        Stack<Node> stack = new Stack<>();
        stack.push(root);
        while (!stack.isEmpty()) {
            Node current = stack.pop();
            if (current.children instanceof ArrayList) {
                for (int i = current.children.size() - 1; i >= 0; i -= 1) {
                    stack.push(current.children.get(i));
                }
            }
            result.add(current.val);
        }
        return result;
    }
}

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        Node node1 = new Node(1);
        Node node3 = new Node(3);
        Node node2 = new Node(2);
        Node node4 = new Node(4);
        Node node5 = new Node(5);
        Node node6 = new Node(6);
        List<Node> list1 = new ArrayList<>();
        list1.add(node3);
        list1.add(node2);
        list1.add(node4);
        List<Node> list2 = new ArrayList<>();
        list2.add(node5);
        list2.add(node6);
        node1.children = list1;
        node3.children = list2;
        System.out.println(solution.preorder(node1));
    }

}

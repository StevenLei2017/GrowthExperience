import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int val) {
        this.val = val;
    }
}

class Solution {

    private int min = 0;
    private int max = 0;

    private class NodeAndIndex {
        TreeNode treeNode;
        int index;

        NodeAndIndex(TreeNode treeNode, int index) {
            this.treeNode = treeNode;
            this.index = index;
        }
    }

    public List<List<Integer>> verticalOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        if (root == null) {
            return result;
        }
        this.helper(root, 0);
        for (int i = this.min; i <= this.max; i += 1) {
            result.add(new ArrayList<>());
        }
        Queue<NodeAndIndex> queue = new LinkedList<>();
        queue.add(new NodeAndIndex(root, 0 - this.min));
        while (!queue.isEmpty()) {
            NodeAndIndex nodeAndIndex = queue.poll();
            TreeNode treeNode = nodeAndIndex.treeNode;
            int index = nodeAndIndex.index;
            result.get(index).add(treeNode.val);
            if (treeNode.left != null) {
                queue.offer(new NodeAndIndex(treeNode.left, index - 1));
            }
            if (treeNode.right != null) {
                queue.offer(new NodeAndIndex(treeNode.right, index + 1));
            }
        }
        return result;
    }

    private void helper(TreeNode root, int index) {
        this.min = Math.min(this.min, index);
        this.max = Math.max(this.max, index);
        if (root.left != null) {
            this.helper(root.left, index - 1);
        }
        if (root.right != null) {
            this.helper(root.right, index + 1);
        }
    }

}

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        TreeNode treeNode_1 = new TreeNode(3);
        TreeNode treeNode_2 = new TreeNode(9);
        TreeNode treeNode_3 = new TreeNode(20);
        TreeNode treeNode_4 = new TreeNode(15);
        TreeNode treeNode_5 = new TreeNode(7);
        treeNode_1.left = treeNode_2;
        treeNode_1.right = treeNode_3;
        treeNode_3.left = treeNode_4;
        treeNode_3.right = treeNode_5;
        List<List<Integer>> result = solution.verticalOrder(treeNode_1);
        System.out.println(result);
    }

}

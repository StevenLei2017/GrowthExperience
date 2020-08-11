class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        this.val = x;
    }
}

class Solution {

    int result;
    TreeNode pre;

    public int minDiffInBST(TreeNode root) {
        this.result = Integer.MAX_VALUE;
        this.helper(root);
        return this.result;
    }

    private void helper(TreeNode root) {
        if (root == null) {
            return;
        }
        this.helper(root.left);
        if (this.pre != null) {
            this.result = Math.min(this.result, root.val - this.pre.val);
        }
        this.pre = root;
        this.helper(root.right);
    }

}

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        TreeNode treeNode1 = new TreeNode(1);
        TreeNode treeNode2 = new TreeNode(2);
        TreeNode treeNode3 = new TreeNode(3);
        treeNode1.right = treeNode3;
        treeNode3.left = treeNode2;
        int result = solution.minDiffInBST(treeNode1);
        System.out.println(result);
    }

}

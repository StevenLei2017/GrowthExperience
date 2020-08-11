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

    public int sumOfLeftLeaves(TreeNode root) {
        this.result = 0;
        this.helper(root);
        return this.result;
    }

    private void helper(TreeNode root) {
        if (root == null) {
            return;
        }
        if (root.left != null && root.left.left == null && root.left.right == null) {
            this.result += root.left.val;
            this.helper(root.right);
        } else {
            this.helper(root.left);
            this.helper(root.right);
        }
    }
    
}

public class Main {

    public static void main(String[] args) {
        TreeNode treeNode1 = new TreeNode(3);
        TreeNode treeNode9 = new TreeNode(9);
        TreeNode treeNode20 = new TreeNode(20);
        TreeNode treeNode15 = new TreeNode(15);
        TreeNode treeNode7 = new TreeNode(7);
        treeNode1.left = treeNode9;
        treeNode1.right = treeNode20;
        treeNode20.left = treeNode15;
        treeNode20.right = treeNode7;
        Solution solution = new Solution();
        int result = solution.sumOfLeftLeaves(treeNode1);
        System.out.println(result);
    }

}

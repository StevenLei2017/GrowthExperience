class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        this.val = x;
    }

}

class Solution {

    public boolean isSubtree(TreeNode s, TreeNode t) {
        if (s == null) {
            return false;
        }
        if (this.isSameTree(s, t)) {
            return true;
        }
        return this.isSubtree(s.left, t) || this.isSubtree(s.right, t);
    }

    private boolean isSameTree(TreeNode s, TreeNode t) {
        if (s == null && t == null) {
            return true;
        }
        if (s == null || t == null) {
            return false;
        }
        if (s.val != t.val) {
            return false;
        }
        return this.isSameTree(s.left, t.left) && this.isSameTree(s.right, t.right);
    }

}

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        TreeNode treeNode1 = new TreeNode(1);
        TreeNode treeNode2 = new TreeNode(2);
        TreeNode treeNode3 = new TreeNode(3);
        TreeNode treeNode4 = new TreeNode(4);
        TreeNode treeNode5 = new TreeNode(5);
        treeNode3.left = treeNode4;
        treeNode3.right = treeNode5;
        treeNode4.left = treeNode1;
        treeNode4.right = treeNode2;
        TreeNode treeNode24 = new TreeNode(4);
        TreeNode treeNode21 = new TreeNode(1);
        TreeNode treeNode22 = new TreeNode(2);
        treeNode24.left = treeNode21;
        treeNode24.right = treeNode22;
        boolean result = solution.isSubtree(treeNode3, treeNode24);
        System.out.println(result);
    }

}

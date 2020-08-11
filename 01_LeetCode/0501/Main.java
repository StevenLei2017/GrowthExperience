import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        this.val = x;
    }
}

class Solution {

    Integer pre = null;
    int count = 1;
    int max = 0;
    List<Integer> list;

    public int[] findMode(TreeNode root) {
        if (root == null) {
            return new int[0];
        }
        this.list = new ArrayList<>();
        this.helper(root);
        return this.list.stream().mapToInt(Integer::intValue).toArray();
    }

    private void helper(TreeNode root) {
        if (root == null) {
            return;
        }
        this.helper(root.left);
        if (this.pre != null) {
            if (root.val == this.pre) {
                this.count += 1;
            } else {
                this.count = 1;
            }
        }
        if (this.count > this.max) {
            this.max = this.count;
            this.list.clear();
            this.list.add(root.val);
        } else if (this.count == this.max) {
            this.list.add(root.val);
        }
        this.pre = root.val;
        this.helper(root.right);
    }

}

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        TreeNode treeNode1 = new TreeNode(1);
        TreeNode treeNode11 = new TreeNode(1);
        TreeNode treeNode2 = new TreeNode(2);
        TreeNode treeNode22 = new TreeNode(2);
        treeNode1.left = treeNode11;
        treeNode1.right = treeNode2;
        treeNode2.left = treeNode22;
        int[] result = solution.findMode(treeNode1);
        System.out.println(Arrays.toString(result));
    }

}

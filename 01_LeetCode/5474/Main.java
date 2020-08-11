import java.util.ArrayList;
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

    List<String> list;

    public int countPairs(TreeNode root, int distance) {
        if (root == null || (root.left == null && root.right == null)) {
            return 0;
        }
        this.list = new ArrayList<>();
        this.helper(root, "0");
        int count = 0;
        for (int i = 0; i < this.list.size(); i += 1) {
            for (int j = i + 1; j < this.list.size(); j += 1) {
                if (this.getDistance(this.list.get(i), this.list.get(j)) <= distance) {
                    count += 1;
                }
            }
        }
        return count;
    }

    private int getDistance(String s1, String s2) {
        int length1 = s1.length();
        int length2 = s2.length();
        int i = 0;
        while (i < length1 && i < length2) {
            if (s1.charAt(i) == s2.charAt(i)) {
                i += 1;
                continue;
            }
            break;
        }
        return length1 + length2 - i * 2;
    }

    private void helper(TreeNode root, String path) {
        if (root.left == null && root.right == null) {
            this.list.add(path);
            return;
        }
        if (root.left != null) {
            this.helper(root.left, path + "0");
        }
        if (root.right != null) {
            this.helper(root.right, path + "1");
        }
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
        TreeNode treeNode6 = new TreeNode(6);
        TreeNode treeNode7 = new TreeNode(7);
        treeNode1.left = treeNode2;
        treeNode1.right = treeNode3;
        treeNode2.left = treeNode4;
        treeNode2.right = treeNode5;
        treeNode3.left = treeNode6;
        treeNode3.right = treeNode7;
        int result = solution.countPairs(treeNode1, 4);
        System.out.println(result);
        TreeNode treeNode84 = new TreeNode(84);
        TreeNode treeNode80 = new TreeNode(80);
        TreeNode treeNode61 = new TreeNode(61);
        treeNode1.left = treeNode84;
        treeNode1.right = null;
        treeNode84.left = treeNode80;
        treeNode84.right = treeNode61;
        result = solution.countPairs(treeNode1, 4);
        System.out.println(result);
    }

}

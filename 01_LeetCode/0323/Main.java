import java.util.Arrays;

class Solution {

    public int countComponents(int n, int[][] edges) {
        int result = n;
        int[] roots = new int[n];
        Arrays.fill(roots, -1);
        for (int[] edge : edges) {
            int index0 = this.find(roots, edge[0]);
            int index1 = this.find(roots, edge[1]);
            if (index0 != index1) {
                roots[index0] = index1;
                result -= 1;
            }
        }
        return result;
    }

    private int find(int[] roots, int i) {
        while (roots[i] != -1) {
            i = roots[i];
        }
        return i;
    }

}

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[][] testCase = {{0, 1}, {1, 2}, {3, 4}};
        int result = solution.countComponents(5, testCase);
        System.out.println(result);
    }

}

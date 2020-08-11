import java.util.Arrays;

class Solution {

    public int findContentChildren(int[] g, int[] s) {
        int result = 0;
        Arrays.sort(g);
        Arrays.sort(s);
        int i = 0, j = 0;
        while (i < g.length && j < s.length) {
            if (g[i] <= s[j]) {
                result++;
                i++;
                j++;
            } else {
                j++;
            }
        }
        return result;
    }

}

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] g = {1, 2};
        int[] s = {1, 2, 3};
        int result = solution.findContentChildren(g, s);
        System.out.println(result);
    }

}

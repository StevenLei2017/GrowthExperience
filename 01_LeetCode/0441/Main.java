class Solution {
    public int arrangeCoins(int n) {
        int x = (int) Math.sqrt(n * 2.0);
        if ((long) x * (x + 1) / 2 <= n) {
            return x;
        } else {
            return x - 1;
        }
    }
}

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        int result = solution.arrangeCoins(5);
        System.out.println(result);
        result = solution.arrangeCoins(6);
        System.out.println(result);
        result = solution.arrangeCoins(1804289383);
        System.out.println(result);
    }

}

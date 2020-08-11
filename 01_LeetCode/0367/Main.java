class Solution {
    public boolean isPerfectSquare(int num) {
        long x = Math.max(num / 2, 1);
        while (x * x > num) {
            x = (x + num / x) / 2;
        }
        return x * x == num;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        boolean result = solution.isPerfectSquare(14);
        System.out.println(result);
        result = solution.isPerfectSquare(16);
        System.out.println(result);
        result = solution.isPerfectSquare(1);
        System.out.println(result);
        result = solution.isPerfectSquare(808201);
        System.out.println(result);
    }
}

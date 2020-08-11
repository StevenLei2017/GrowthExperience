class Solution {

    public boolean checkPerfectNumber(int num) {
        if (num == 1) {
            return false;
        }
        int sum = 0;
        for (int i = 2; i <= (int) Math.sqrt(num); i++) {
            if (num % i == 0) {
                sum += i + num / i;
            }
        }
        sum += 1;
        return sum == num;
    }

}

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        boolean result = solution.checkPerfectNumber(28);
        System.out.println(result);
        result = solution.checkPerfectNumber(27);
        System.out.println(result);
        result = solution.checkPerfectNumber(6);
        System.out.println(result);
    }

}

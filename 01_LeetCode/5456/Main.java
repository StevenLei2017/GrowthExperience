class Solution {

    public int countOdds(int low, int high) {
        int result = 0;
        if (low % 2 == 0) {
            if (high == low) {
                return 0;
            } else {
                result = (high - low - 1) / 2 + 1;
                return result;
            }
        }
        if (high == low) {
            return 1;
        } else {
            result = (high - low) / 2 + 1;
            return result;
        }
    }

}

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        int result = solution.countOdds(3, 7);
        System.out.println(result);
        result = solution.countOdds(8, 10);
        System.out.println(result);
    }

}

class Solution {

    public int findComplement(int num) {
        int sum = 0;
        while (sum < num) {
            sum = (sum << 1) | 1;
        }
        return sum - num;
    }

}

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        int testCase = 1;
        int result = solution.findComplement(testCase);
        System.out.println(result);
        testCase = 5;
        result = solution.findComplement(testCase);
        System.out.println(result);
    }

}

class Solution {

    public boolean validPalindrome(String s) {
        int left = 0, right = s.length() - 1;
        while (left < right && s.charAt(left) == s.charAt(right)) {
            left += 1;
            right -= 1;
        }
        return this.isPalindrome(s, left, right - 1) || this.isPalindrome(s, left + 1, right);
    }

    public boolean isPalindrome(String s, int left, int right) {
        while (left < right && s.charAt(left) == s.charAt(right)) {
            left += 1;
            right -= 1;
        }
        if (left >= right) {
            return true;
        }
        return false;
    }

}

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        String testCase = "aba";
        boolean result = solution.validPalindrome(testCase);
        System.out.println(result);
        testCase = "abca";
        result = solution.validPalindrome(testCase);
        System.out.println(result);
    }

}

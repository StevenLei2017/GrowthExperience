class Solution {

    public String reverseStr(String s, int k) {
        StringBuilder stringBuilder = new StringBuilder(s);
        if (s == null || s.length() <= 1) {
            return s;
        }
        int index = 0;
        while (index < s.length()) {
            this.helper(s, index, index + k - 1, stringBuilder);
            index += k * 2;
        }
        return stringBuilder.toString();
    }

    private void helper(String s, int left, int right, StringBuilder stringBuilder) {
        right = Math.min(right, s.length() - 1);
        while (left < right) {
            char temp = stringBuilder.charAt(left);
            stringBuilder.setCharAt(left, stringBuilder.charAt(right));
            stringBuilder.setCharAt(right, temp);
            left += 1;
            right -= 1;
        }
    }

}


public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        String s = "abcdefg";
        String result = solution.reverseStr(s, 2);
        System.out.println(result);
    }

}

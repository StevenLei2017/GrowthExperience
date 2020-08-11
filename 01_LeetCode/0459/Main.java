class Solution {
    public boolean repeatedSubstringPattern(String s) {
        String str = s + s;
        return str.substring(1, s.length() * 2 - 1).contains(s);
    }
}

public class Main {

    public static void main(String[] args) {
        String s = "abab";
        Solution solution = new Solution();
        boolean result = solution.repeatedSubstringPattern(s);
        System.out.println(result);
    }

}

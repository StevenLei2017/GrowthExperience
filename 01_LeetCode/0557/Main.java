class Solution {

    public String reverseWords(String s) {
        if (s == null || s.length() == 0) {
            return s;
        }
        StringBuilder stringBuilder = new StringBuilder();
        String[] words = s.split(" ");
        for (int i = 0; i < words.length - 1; i += 1) {
            String word = words[i];
            stringBuilder.append(new StringBuilder(word).reverse().toString() + " ");
        }
        stringBuilder.append(new StringBuilder(words[words.length - 1]).reverse().toString());
        String result = stringBuilder.toString();
        return result;
    }

}

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        String testCase = "Let's take LeetCode contest";
        String result = solution.reverseWords(testCase);
        System.out.println(result);
    }

}

class Solution {

    public String restoreString(String s, int[] indices) {
        if (s == null || s.length() == 0) {
            return s;
        }
        char[] result = new char[s.length()];
        for (int i = 0; i < s.length(); i += 1) {
            int index = indices[i];
            result[index] = s.charAt(i);
        }
        return String.valueOf(result);
    }

}


public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        String s = "aiohn";
        int[] indices = {3, 1, 4, 2, 0};
        String result = solution.restoreString(s, indices);
        System.out.println(result);
    }

}

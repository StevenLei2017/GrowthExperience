class Solution {

    public int countSegments(String s) {
        if (s == null || s.trim().length() == 0) {
            return 0;
        }
        String[] words = s.trim().split("\\s+");
        return words.length;
    }

}

class Main {

    public static void main(String[] args) {
        String s = "Hello, my name is John";
        Solution solution = new Solution();
        int result = solution.countSegments(s);
        System.out.println(result);
    }

}

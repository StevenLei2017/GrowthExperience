class Solution {
        public char findTheDifference(String s, String t) {
            int[] lettersCount = new int[26];
            for(char c: s.toCharArray()){
                lettersCount[c - 'a'] += 1;
            }
            for(char c: t.toCharArray()){
               if(lettersCount[c - 'a'] == 0){
                   return c;
               }
               lettersCount[c - 'a'] -= 1;
            }
            return 'a';
        }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        String s = "abcd", t = "abcde";
        char result = solution.findTheDifference(s, t);
        System.out.println(result);
    }
}

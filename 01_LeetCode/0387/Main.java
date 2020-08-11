class Solution {
    public int firstUniqChar(String s) {
        int[] lettersCount = new int[26];
        for(char c: s.toCharArray()){
            lettersCount[c - 'a'] += 1;
        }
        for(int i = 0; i < s.length(); i += 1){
            if(lettersCount[s.charAt(i) - 'a'] == 1){
                return i;
            }
        }
        return -1;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        String testCase = "leetcode";
        int result = solution.firstUniqChar(testCase);
        System.out.println(result   );
    }
}

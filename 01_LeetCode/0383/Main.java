class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        int[] lettersCount = new int[26];
        for(char c: magazine.toCharArray()){
            lettersCount[c - 'a'] += 1;
        }
        for(char c: ransomNote.toCharArray()){
            if(lettersCount[c - 'a'] == 0){
                return false;
            }
            lettersCount[c - 'a'] -= 1;
        }
        return true;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        boolean result = solution.canConstruct("aa", "ab");
        System.out.println(result);
    }
}

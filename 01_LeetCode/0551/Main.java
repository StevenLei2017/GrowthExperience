class Solution {

    public boolean checkRecord(String s) {
        int countA = 0, countL = 0;
        for (char c : s.toCharArray()) {
            if (c == 'A') {
                countA += 1;
            }
            if (c == 'L') {
                countL += 1;
            } else {
                countL = 0;
            }
            if (countA >= 2 || countL >= 3) {
                return false;
            }
        }
        return true;
    }

}


public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        String testCase = "PPALLP";
        boolean result = solution.checkRecord(testCase);
        System.out.println(result);
        testCase = "PPALLL";
        result = solution.checkRecord(testCase);
        System.out.println(result);
    }

}

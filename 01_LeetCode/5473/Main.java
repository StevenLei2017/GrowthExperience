class Solution {

    public int minFlips(String target) {
        int count = 0;
        char now = '0';
        for (char c : target.toCharArray()) {
            if (c != now) {
                count += 1;
                now = c;
            }
        }
        return count;
    }

}

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        String target = "001011101";
        int result = solution.minFlips(target);
        System.out.println(result);
    }

}

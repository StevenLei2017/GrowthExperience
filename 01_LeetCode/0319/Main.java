class Solution {

    public int bulbSwitch(int n) {
        int result = (int) Math.sqrt(n);
        return result;
    }

}

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        int result = solution.bulbSwitch(3);
        System.out.println(result);
    }

}

class Solution {

    public String convertToBase7(int num) {
        char[] map = {'0', '1', '2', '3', '4', '5', '6'};
        if (num == 0) {
            return "0";
        }
        StringBuilder stringBuilder = new StringBuilder();
        boolean isPositive = true;
        if (num < 0) {
            isPositive = false;
            num = -num;
        }
        while (num > 0) {
            stringBuilder.append(map[num % 7]);
            num /= 7;
        }
        if (!isPositive) {
            stringBuilder.append('-');
        }
        return stringBuilder.reverse().toString();
    }

}

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        int input;
        String result;
        input = 100;
        result = solution.convertToBase7(input);
        System.out.println(result);
        input = -7;
        result = solution.convertToBase7(input);
        System.out.println(result);
    }

}

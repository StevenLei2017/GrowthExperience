class Solution {
    public String addStrings(String num1, String num2) {
        int i = num1.length() - 1;
        int j = num2.length() - 1;
        int carry = 0;
        StringBuilder stringBuilder = new StringBuilder();
        while (i >= 0 || j >= 0 || carry == 1) {
            int a = i >= 0 ? num1.charAt(i) - '0' : 0;
            int b = j >= 0 ? num2.charAt(j) - '0' : 0;
            i -= 1;
            j -= 1;
            int sum = a + b + carry;
            stringBuilder.append(sum % 10);
            carry = sum / 10;
        }
        return stringBuilder.reverse().toString();
    }
}

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        String s1 = "51234";
        String s2 = "57689";
        String result = solution.addStrings(s1, s2);
        System.out.println(result);
    }

}

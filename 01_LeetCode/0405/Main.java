class Solution {

    char[] map = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'};

    public String toHex(int num) {
        if (num == 0) {
            return "0";
        }
        StringBuilder stringBuilder = new StringBuilder();
        while (num != 0) {
            stringBuilder.append(this.map[num & 15]);
            num >>>= 4;
        }
        return stringBuilder.reverse().toString();
    }
    
}


public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        String result = solution.toHex(-1);
        System.out.println(result);
    }

}

class Solution {
    public int hammingDistance(int x, int y) {
        return Integer.bitCount(x ^ y);
    }
}


public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        int result = solution.hammingDistance(5, 4);
        System.out.println(result);
    }

}

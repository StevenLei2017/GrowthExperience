import java.util.Arrays;

class Solution {

    public int[] constructRectangle(int area) {
        int W = (int) Math.sqrt(area);
        while (area % W != 0) {
            W -= 1;
        }
        return new int[]{area / W, W};
    }

}


public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] result = solution.constructRectangle(4);
        System.out.println(Arrays.toString(result));
        result = solution.constructRectangle(6);
        System.out.println(Arrays.toString(result));
        result = solution.constructRectangle(7);
        System.out.println(Arrays.toString(result));
    }

}

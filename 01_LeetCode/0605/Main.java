class Solution {

    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        if (n == 0) {
            return true;
        }
        if (flowerbed.length == 1 && flowerbed[0] == 0 && n == 1) {
            return true;
        }
        if (flowerbed.length >= 2 && flowerbed[1] == 0 && flowerbed[0] == 0) {
            flowerbed[0] = 1;
            n -= 1;
        }
        if (flowerbed.length >= 2 && flowerbed[flowerbed.length - 1] == 0 && flowerbed[flowerbed.length - 2] == 0) {
            flowerbed[flowerbed.length - 1] = 1;
            n -= 1;
        }
        for (int i = 1; i < flowerbed.length - 1; i += 1) {
            if (flowerbed[i] == 0 && flowerbed[i - 1] == 0 && flowerbed[i + 1] == 0) {
                flowerbed[i] = 1;
                n -= 1;
                if (n == 0) {
                    break;
                }
            }
        }
        if (n <= 0) {
            return true;
        }
        return false;
    }

}


public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] flowerbed = {1, 0, 0, 0, 1};
        boolean result = solution.canPlaceFlowers(flowerbed, 1);
        System.out.println(result);
        result = solution.canPlaceFlowers(flowerbed, 2);
        System.out.println(result);
        flowerbed = new int[]{0, 0, 1, 0, 1};

    }

}

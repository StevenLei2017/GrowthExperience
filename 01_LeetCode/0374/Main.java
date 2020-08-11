class GuessGame {

    private int value;

    GuessGame(int value) {
        this.value = value;
    }

    public int guess(int x) {
        if (x == this.value) {
            return 0;
        } else if (x < this.value) {
            return 1;
        } else {
            return -1;
        }
    }
}

class Solution extends GuessGame {
    Solution(int value) {
        super(value);
    }

    public int guessNumber(int n) {
        if (this.guess(n) == 1) {
            return -1;
        }
        int left = 0, right = n;
        while (left <= right) {
            int middle = left + (right - left) / 2;
            int result = this.guess(middle);
            if (result == 0) {
                return middle;
            } else if (result == -1) {
                right = middle - 1;
            } else {
                left = middle + 1;
            }
        }
        return -1;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution(1702766719);
        int result = solution.guessNumber(2126753390);
        System.out.println(result);
    }
}

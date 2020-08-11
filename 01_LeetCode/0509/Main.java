class Solution {

    int[] fibonaccis = new int[31];

    Solution() {
        this.fibonaccis[0] = 0;
        this.fibonaccis[1] = 1;
        this.fibonaccis[2] = 1;
        for (int i = 3; i <= 30; i += 1) {
            this.fibonaccis[i] = this.fibonaccis[i - 1] + this.fibonaccis[i - 2];
        }
    }

    public int fib(int N) {
        return this.fibonaccis[N];
    }

}

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        int result = solution.fib(2);
        System.out.println(result);
        result = solution.fib(3);
        System.out.println(result);
        result = solution.fib(4);
        System.out.println(result);
        result = solution.fib(29);
        System.out.println(result);
        result = solution.fib(30);
        System.out.println(result);
    }

}

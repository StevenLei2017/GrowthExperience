import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;

class Solution {

    public int nthSuperUglyNumber(int n, int[] primes) {
        int[] result = new int[n];
        int[] indexes = new int[primes.length];
        result[0] = 1;
        for (int i = 1; i < n; i += 1) {
            List<Integer> list = new ArrayList<>();
            int min = Integer.MAX_VALUE;
            for (int j = 0; j < primes.length; j += 1) {
                int index = indexes[j];
                int number = result[index] * primes[j];
                list.add(number);
                min = Math.min(min, number);
            }
            result[i] = min;
            for (int j = 0; j < primes.length; j += 1) {
                int index = indexes[j];
                if (min == result[index] * primes[j]) {
                    indexes[j] += 1;
                }
            }
        }
        return result[n - 1];
    }

    public int nthSuperUglyNumber2(int n, int[] primes) {
        int[] result = new int[n];
        result[0] = 1;
        PriorityQueue<Num> priorityQueue = new PriorityQueue<>((a, b) -> a.val - b.val);
        for (int i = 0; i < primes.length; i += 1) {
            int prime = primes[i];
            priorityQueue.add(new Num(prime, 1, prime));
        }
        for (int i = 1; i < n; i += 1) {
            result[i] = priorityQueue.peek().val;
            while (result[i] == priorityQueue.peek().val) {
                Num next = priorityQueue.poll();
                priorityQueue.add(new Num(next.prime * result[next.index], next.index + 1, next.prime));
            }
        }
        return result[n - 1];
    }

    class Num {
        int val;
        int index;
        int prime;

        Num(int val, int index, int prime) {
            this.val = val;
            this.index = index;
            this.prime = prime;
        }
    }

}

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        int n = 12;
        int[] primes = {2, 7, 13, 19};
        int result = solution.nthSuperUglyNumber(n, primes);
        System.out.println(result);
    }

}

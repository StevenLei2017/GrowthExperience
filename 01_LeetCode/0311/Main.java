import java.util.Arrays;

class Solution {

    public int[][] multiply(int[][] A, int[][] B) {
        int m = A.length, n = A[0].length;
        int nB = B[0].length;
        int[][] result = new int[m][nB];
        for (int i = 0; i < m; i += 1) {
            for (int k = 0; k < n; k += 1) {
                if (A[i][k] != 0) {
                    for (int j = 0; j < nB; j += 1) {
                        if (B[k][j] != 0) {
                            result[i][j] += A[i][k] * B[k][j];
                        }
                    }
                }
            }
        }
        return result;
    }

}

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[][] A = {{1, 0, 0}, {-1, 0, 3}};
        int[][] B = {{7, 0, 0}, {0, 0, 0}, {0, 0, 1}};
        int[][] result = solution.multiply(A, B);
        for (int[] row : result) {
            System.out.println(Arrays.toString(row));
        }
    }

}

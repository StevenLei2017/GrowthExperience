class Solution {

    public int islandPerimeter(int[][] grid) {
        int islands = 0;
        int neighbours = 0;
        for(int i = 0; i < grid.length; i += 1){
            for(int j = 0; j < grid[0].length; j += 1){
                if(grid[i][j] == 1){
                    islands += 1;
                    if(j < grid[0].length - 1 && grid[i][j + 1] == 1){
                        neighbours += 1;
                    }
                    if(i < grid.length - 1 && grid[i+ 1][j] == 1){
                        neighbours += 1;
                    }
                }
            }
        }
        int result = islands * 4 - neighbours * 2;
        return result;
    }

}

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[][] grid = {
                {0, 1, 0, 0},
                {1, 1, 1, 0},
                {0, 1, 0, 0},
                {1, 1, 0, 0}
        };
        int result = solution.islandPerimeter(grid);
        System.out.println(result);
    }

}

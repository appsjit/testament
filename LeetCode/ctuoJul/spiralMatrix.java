// package whatever; // don't place package name!
/*
Matrices - N Spiral Matrix
Prompt
Given an integer N, output an N x N spiral matrix with integers 1 through N2.

Examples:
Input:  3

Output: [[1, 2, 3],
         [8, 9, 4],
         [7, 6, 5]

Input: 1

Output: [[1]]

Input:
n = {Integer}

Output
result = {Integer[][]}
*/
import java.io.*;
import java.util.Arrays;

class MyCode {
  public static int[][] spiralMatrix(int n) {
    if (n < 1) return new int[0][];

    int[][] matrix = new int[n][n];
    int minRow = 0, maxRow = n-1, minCol = 0, maxCol = n-1, count = 1;
    while (minRow <= maxRow && minCol <= maxCol) {
      // traverse to the right
      for (int col = minCol; col <= maxCol; col++) {
        matrix[minRow][col] = count;
        count++;
      }
      minRow++;

      // traverse down from top to bottom
      for (int row = minRow; row <= maxRow; row++) {
        matrix[row][maxCol] = count;
        count++;
      }
      maxCol--;

      // traverse left
      for (int col = maxCol; col >= minCol; col--) {
        matrix[maxRow][col] = count;
        count++;
      }
      maxRow--;

      // traverse up
      for (int row = maxRow; row >= minRow; row--) {
        matrix[row][minCol] = count;
        count++;
      }
      minCol++;

    }
    return matrix;
  }

  public static void printMatrix(int[][] matrix) {
    // String output = "[";
    for (int row = 0; row < matrix.length; row++) {
      System.out.println(Arrays.toString(matrix[row]));
    }
  }
	public static void main (String[] args) {
    int[][] result1 = spiralMatrix(3);
    printMatrix(result1);
    System.out.println();

    int[][] result2 = spiralMatrix(1);
    printMatrix(result2);
    System.out.println();

    int[][] result3 = spiralMatrix(5);
    printMatrix(result3);
		// System.out.println("spiralMatrix(3) = " + );
	}
}

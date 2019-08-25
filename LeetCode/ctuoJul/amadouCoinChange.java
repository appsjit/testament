// package whatever; // don't place package name!
/*
Dynamic Programming - Minimum Coin Change
Prompt:
You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make
up that amount. If that amount of money cannot be made up by any combination of
the coins, return -1.

Examples:
Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.
*/
import java.io.*;
import java.util.Arrays;

class MyCode {
  public static int coinChange(int[] coins, int amount) {
    int max = amount+1;
    int[] res = new int[max];
    Arrays.fill(res, max);
    res[0] = 0;
    for (int i = 1; i <= amount; i++) {
      for (int j = 0; j < coins.length; j++) {
        int remainingAmount = i - coins[j];
        if (remainingAmount >= 0) {
          res[i] = Math.min(res[i], 1 + res[remainingAmount]);
        }
      }
    }
    return (res[amount] == max) ? -1 : res[amount];
  }
	public static void main (String[] args) {
    int[] coins = {1, 2, 5}, coins1 = {2};
		System.out.println("coinChange([1,2,5], 11) = " + coinChange(coins, 11));
    System.out.println("coinChange([2], 3) = " + coinChange(coins1, 3));
	}
}

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package LeetCodeJava;

/**
 *
 * @author abhijitrode
 */
public class s_0918_MaxSumCircularArray {
    public int maxSubarraySumCircular(int[] nums) {
        int S = 0;
        for (int x: nums)
            S += x;   
        System.out.println("S :"+S);
        
        int maxSum = Integer.MIN_VALUE;
        int cur = Integer.MIN_VALUE;
        
        // Answer for non circular array
        for (int x : nums){
            cur = x + Math.max(0, cur);
            maxSum = Math.max(maxSum, cur);
        }
        
        System.out.println("maxSum :"+maxSum);
        int minSum = nums[0];
        cur = 0;
        
        // Ans with Min
        for (int x : nums){
            cur = x + Math.min(0, cur);
            minSum = Math.min(minSum, cur);
            //System.out.println("cur :"+cur+"   minSum:"+minSum);
        } 
        System.out.println("minSum :"+minSum);
        minSum = S - minSum;
        if (minSum == 0){
            return maxSum;
        }
        
        return Math.max(maxSum, minSum);
        

    }
}

// class Solution {
//     public int maxSubarraySumCircular(int[] nums) {
//         int probableAns = maxSubArraySum(nums);
//         int anotherProbableAns = arraySum(nums) - minSubArraySum(nums);
//         if (anotherProbableAns == 0) { // entire array is negative
//             return probableAns;
//         }
//         return Math.max(probableAns, anotherProbableAns);
//     }
    
//     int arraySum(int[] nums) {
//         return Arrays.stream(nums)
//             .reduce(0, Integer::sum);
//     }
    
//     // kadane algo 
//     int maxSubArraySum(int[] nums) {
//         int currSum = 0, maxSum = nums[0];
//         for(int num: nums) {
//             if (currSum < 0) {
//                 currSum = 0;
//             }
//             currSum += num;
//             maxSum = Math.max(currSum, maxSum);
//         }
//         return maxSum;
//     }
    
//     // kadane algo
//     int minSubArraySum(int[] nums) {
//         int currSum = 0, minSum = nums[0];
//         for(int num: nums) {
//             if (currSum > 0) {
//                 currSum = 0;
//             }
//             currSum += num;
//             minSum = Math.min(currSum, minSum);
//         }
//         return minSum;
//     }
// }

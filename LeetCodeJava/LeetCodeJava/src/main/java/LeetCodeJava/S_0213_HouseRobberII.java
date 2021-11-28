/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package LeetCodeJava;

import java.util.Arrays;

/**
 *
 * @author abhijitrode
 */
public class S_0213_HouseRobberII {
         private int helper(int[] pNums){
            int L = pNums.length;



            int oddCnt = 0;
            int evenCnt = 0;

            for (int i = 0; i < L ; i++){
                int temp = oddCnt;
                oddCnt = Math.max(evenCnt + pNums[i], oddCnt);
                evenCnt = temp; 
            }


            return Math.max(evenCnt, oddCnt);
        }
    
    public int rob(int[] nums) {

        int L = nums.length;
        if(L == 1)
            return nums[0];
        // Take houses from first to second last  and compare with second to last
        int t1 = helper(Arrays.copyOfRange(nums, 0, L-1));
        int t2 = helper(Arrays.copyOfRange(nums, 1, L)); 
        return Math.max(t1, t2);
    }   
}

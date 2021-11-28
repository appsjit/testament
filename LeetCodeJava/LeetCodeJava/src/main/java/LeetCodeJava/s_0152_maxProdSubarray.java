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
public class s_0152_maxProdSubarray {
    public int maxProduct(int[] nums) {
        /*
        2 3 -2 4
        2 6 6 6
        2 6 -12
        */
        if (nums.length == 1)
            return nums[0];
        else if (nums.length == 0)
            return 0;
        int ans = 0;
        int maxPossible = 0;
        int minPossible = 0;
        // System.out.println(maxPossible);
        // System.out.println(minPossible);
        for (int x : nums){
            System.out.println(x);
            if (x >= 0){
                maxPossible = x * Math.max(1 ,maxPossible); 
                minPossible = x * Math.min(1, minPossible);
            } else if (x < 0){
                // Hold Possible max value before modifying minPossible Value
                // if x = 0 then maxPossible will be zero else -ve -ve big +ve
                int temp = Math.max(x, x*minPossible);
                // +ve value will be flipping if x 0 then 0 else -ve
                minPossible = Math.min(x ,x*maxPossible);
                maxPossible = temp; 
            }
            ans = Math.max(ans, maxPossible);
        }
        System.out.println("ans:"+ans);
        return ans;
    }
}

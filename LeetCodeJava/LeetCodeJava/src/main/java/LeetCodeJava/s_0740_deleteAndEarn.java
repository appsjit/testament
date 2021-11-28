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
public class s_0740_deleteAndEarn {
    public int deleteAndEarn(int[] nums) {
        //Arrays.sort(nums);
        
        int[] baseNumbers = new int[10001]; // Taking as Top limit
        
        int cntOdd = 0;
        int cntEven = 0;
        
        // Assign all numbers repetitions in array 
        // eg. 3, 4, 3  array.  [0, 0, 0, 2, 1]
        for (int x : nums){
            baseNumbers[x] += 1; 
        }
        
        // Check alternate which combination will make it max 
        // Converted to HouseRobber problem
        for (int j = 0;j < 10001;j++){
            int temp = cntOdd;
            cntOdd = Math.max(j*baseNumbers[j] + cntEven, cntOdd);
            cntEven = temp;
        }
            
        return Math.max(cntEven, cntOdd);
    }   
}

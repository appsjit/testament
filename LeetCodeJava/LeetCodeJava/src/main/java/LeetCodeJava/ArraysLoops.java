/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package LeetCodeJava;

import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

/**
 *
 * @author abhijitrode
 */
public class ArraysLoops {
        public static void main(String[] args) {
        //int[] matchsticks = {1,1,2,2,3};//new int[5];
        int[] matchsticks = new int[]{1,1,2,2,3};
        
        // 1
        int[] descArr1 = Arrays.stream(matchsticks)
        .boxed()
        .sorted(Comparator.reverseOrder()) // just use 'sorted()' for ascending order
        .mapToInt(Integer::intValue)
        .toArray();
        
        // 2
        int[] descArr2 = IntStream.of(matchsticks)
                .boxed()
                .sorted((a, b) -> Integer.compare(b, a))
                .mapToInt(Integer::intValue).toArray();
 
        // 3
        int[] descArr3 = IntStream.of(matchsticks)
                .boxed()
                .sorted((a, b) -> b - a)
                .mapToInt(Integer::intValue).toArray();
        
        // 4
        int size = matchsticks.length;
        int[] descArr4 = new int[size];
        Arrays.setAll(descArr4, i -> matchsticks[size - i - 1]);
        
        matchsticks[0] = 1;
        matchsticks[1] = 1;
        matchsticks[2] = 2;
        matchsticks[3] = 2;
        //matchsticks[4] = 2;
        
        
        Integer[] matchInteger = new Integer[]{5,6,7,7,6};
        Arrays.sort(matchInteger, Collections.reverseOrder());
        
        for (int side : descArr3)   {
            System.out.println("TBD :"+side);
        }
        
        
        int[] intArray = new int[]{1,1,2,2,3};
        //int array to Integer List
        List<Integer> integerList;
            integerList = Arrays.stream(intArray).boxed().collect(Collectors.toList());
        
        
    }
  
}

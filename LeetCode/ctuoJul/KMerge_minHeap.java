/*
Merge K Sorted Arrays

Given an array of sorted arrays of numbers, return the result of
merging all those sorted arrays into a single sorted array

Input: arrays , Array of Arrays of Ints, [[Int]]
Output: [Int]

Example
Input:
[
[1, 10, 11, 15],
[2, 4,  9],
[5, 6,  8, 14, 16],
[3, 7,  12, 13]
]

Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
*/

import java.io.*;
import java.util.PriorityQueue;
import java.util.Arrays;

class MyCode {

  public static class Tuple implements Comparable<Tuple> {
    int[] array;
    int index;

    public Tuple(int[] array, int index) {
      this.array = array;
      this.index = index;
    }

    @Override
    public int compareTo(Tuple t) {
      return this.array[this.index] - t.array[t.index];
    }
  }

  public static int[] mergeKSortedArrays(int[][] arrays) {
    PriorityQueue<Tuple> minHeap = new PriorityQueue<>();
    int totalLength =0;

    for (int row = 0; row < arrays.length; row++) {
      Tuple current = new Tuple(arrays[row],0);
      minHeap.add(current);
      totalLength += arrays[row].length;
    }

    int[] result = new int[totalLength];
    int k = 0;

    while (!minHeap.isEmpty()) {
      Tuple topTuple = minHeap.remove();
      result[k] = topTuple.array[topTuple.index];
      k++;
      // add the next element from same array if index is less than the length of current array
      if (topTuple.index < topTuple.array.length-1) {
        Tuple nextTuple = new Tuple(topTuple.array, topTuple.index+1);
        minHeap.add(nextTuple);
      }
    }
    return result;

  }

	public static void main (String[] args) {
//     [1, 10, 11, 15],
// [2, 4,  9],
// [5, 6,  8, 14, 16],
// [3, 7,  12, 13]
    int[][] arrays = {{1, 10, 11, 15}, {2, 4,  9}, {5, 6,  8, 14, 16}, {3, 7,  12, 13}};
		System.out.println(Arrays.toString(mergeKSortedArrays(arrays)));
	}
}
























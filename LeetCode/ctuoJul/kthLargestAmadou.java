
/*
Leetcode 215:
Find the kth largest element in an unsorted array. Note that it is the kth
largest element in the sorted order, not the kth distinct element.

Example 1:
Input: [3,2,1,5,6,4] and k = 2
Output: 5


Example 2:
Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
*/
import java.io.*;
import java.util.*;

class MyCode {

  public static int findKthLargest(int[] arr, int k) {
    if (arr == null || arr.length == 0) return -1;

    PriorityQueue<Integer> minHeap = new PriorityQueue<>(k);

    for (int i = 0; i < k; i++) {
      minHeap.add(arr[i]);
    }

    for (int i = k; i < arr.length; i++) {
      if (arr[i] > minHeap.peek()) {
        minHeap.remove();
        minHeap.add(arr[i]);
      }
    }

    return minHeap.peek();
  }

  public static int findKthLargest2(int[] arr, int k) {
    if (arr == null || arr.length == 0) return -1;
    int n = arr.length, left = 0, right = n-1, indexOfK = n-k;
    while (left < right) {
      int pivot = quickSelect(arr, left, right);
      if (pivot == indexOfK) return arr[pivot];
      else if (pivot < indexOfK) left = pivot+1;
      else right = pivot -1;
    }
    return arr[left];
  }

  public static int quickSelect(int[] arr, int left, int right) {
    int n = arr.length, pivot = right, wall = left;
    for (int i = left; i < pivot; i++) {
      if (arr[i] < arr[pivot]) {
        swap(arr, wall, i);
        wall++;
      }
    }
    swap(arr, wall, pivot);
    return wall;
  }

  private static void swap(int[] arr, int i, int j){
    int temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
  }

	public static void main (String[] args) {
    int[] arr1 = {3,2,1,5,6,4}, arr2 = {3,2,3,1,2,4,5,5,6};

		System.out.println("findKthLargest([3,2,1,5,6,4], 2) = " + findKthLargest(arr1, 2));
    System.out.println("findKthLargest([3,2,3,1,2,4,5,5,6], 4) = " + findKthLargest(arr2, 4));

    System.out.println("findKthLargest2([3,2,1,5,6,4], 2) = " + findKthLargest2(arr1, 2));
    System.out.println("findKthLargest2([3,2,3,1,2,4,5,5,6], 4) = " + findKthLargest2(arr2, 4));
	}
}





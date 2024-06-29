package LeetCode.Easy;

/*
 * Date: 6/28/2024
 * Given an array of integers nums and an integer target, 
 * return indices of the two numbers such that they add up to target.
 * Example:
 * Input: nums = [3,2,4], target = 6
 * Output: [1,2]
 */

class TwoSum {
    public static void main(String[] args) {
        int[] myArray = { 2, 7, 11, 15 };
        int target = 18;
        twoSum(myArray, target);

    }

    public static int[] twoSum(int[] myArray, int target) {
        for (int i = 0; i < myArray.length - 1; i++) {
            for (int j = i + 1; j < myArray.length; j++) {
                if (myArray[i] + myArray[j] == target) {
                    // System.out.println("[ " + myArray[i] + ", " + myArray[j] + "]");
                    return new int[] { myArray[i], myArray[j] };
                }
            }
        }
        return myArray;
    }

}
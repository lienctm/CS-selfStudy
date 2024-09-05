import java.util.*;

public class PlusOne {
    public static void main(String[] args) {
        int[] first = { 1, 2, 9 };
        System.out.println(Arrays.toString(plusOne(first)));

    }

    public static int[] plusOne(int[] digits) {
        int length = digits.length;
        for (int i = length - 1; i >= 0; i--) {
            if (digits[i] < 9) {
                digits[i]++;
                return digits;
            }
            digits[i] = 0;
        }
        int[] newDigits = new int[length + 1];
        newDigits[0] = 1;
        return newDigits;
    }
}

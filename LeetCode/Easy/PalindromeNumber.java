// Date: 8/12/2024
// Given an integer, return true if it is palindrome, and false otherwise.
// Example:
// Input: x = 121
// Output: true

class PalindromeNumber {
    public static void main(String[] args) {
        int num = 121;
        if (isPalindrome(num)) {
            System.out.println(num + " is palindrome number.");
        } else {
            System.out.println(num + " is NOT a palindrome number.");
        }
    }

    public static boolean isPalindrome(int x) {
        // negative number, 10, 20... are not palindrome number
        if (x < 0 || ((x != 0) && (x % 10 == 0))) {
            return false;
        }

        int reverse_num = 0;
        // 1st loop, 121 > 0, reverse_num = 1, x = 12
        // 2nd loop, 12 > 1, reverse_num = 12, x = 1;
        // 3rd loop, 1 < 12, break the loop and return
        while (x > reverse_num) {
            reverse_num = reverse_num * 10 + x % 10;
            x = x / 10;
        }
        return x == reverse_num || x == reverse_num / 10;
    }
}
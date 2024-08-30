/*
 * Date:
 * Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
 * An input string is valid if:
 * 1. Open brackets must be closed by the same type of brackets.
 * 2. Open brackets must be closed in the correct order.
 * 3. Every close bracket has a corresponding open bracket of the same type.
 */

public class ValidParentheses {
    public static void main(String args[]) {
        String test = "()[]{}";
        System.out.println(isValid(test));

    }

    public static boolean isValid(String s) {
        // int length = s.length();
        char[] ch = s.toCharArray();
        int index = 0;
        boolean exit = true;
        while (exit && index < s.length() - 2) {
            if (ch[index] == ch[index + 1]) {
                index = index + 2;
                exit = true;
            }
            exit = false;
        }
        return exit;
    }

}

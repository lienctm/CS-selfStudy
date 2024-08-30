
/*
 * Date:
 * Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
 * An input string is valid if:
 * 1. Open brackets must be closed by the same type of brackets.
 * 2. Open brackets must be closed in the correct order.
 * 3. Every close bracket has a corresponding open bracket of the same type.
 */
import java.util.*;

public class ValidParentheses {
    public static void main(String args[]) {
        String test = "(({}[]))";
        System.out.println(isValid(test));

    }

    public static boolean isValid(String s) {
        Stack<Character> temp = new Stack<Character>();
        for (char c : s.toCharArray()) {
            if (c == '(') {
                temp.push(')');
            } else if (c == '{') {
                temp.push('}');
            } else if (c == '[') {
                temp.push(']');
            } else if (temp.isEmpty() || temp.pop() != c) {
                return false;
            }
        }
        return temp.isEmpty();
    }
}
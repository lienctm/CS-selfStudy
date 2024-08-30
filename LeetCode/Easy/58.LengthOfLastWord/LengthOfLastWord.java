public class LengthOfLastWord {
    public static void main(String[] args) {
        // String test = " fly me to the moon ";
        // String test = "Hello World";
        String test = " a";
        // String test = "a ";
        // String test = "day";
        System.out.println(lengthOfLastWord(test));
    }

    public static int lengthOfLastWord(String s) {
        /** 1st way - my solution, not works for all test cases */
        // int first = 0;
        // int last = 0;
        // int length = 0;
        // for (int i = s.length() - 1; i > 0; i--) {
        // if (s.charAt(i) != ' ') {
        // last = i;
        // for (int j = i; j >= 0; j--) {
        // if (s.charAt(j) == ' ') {
        // first = j;
        // break;
        // }
        // }
        // break;
        // }
        // }
        // if (last == 0 && first == 0) {
        // length = last - first + 1;
        // } else {
        // length = last - first;
        // }
        // return length;

        /** 2nd ways - online solution, works for all test cases */
        String[] words = s.split(" ");
        return words.length == 0 ? 0 : words[words.length - 1].length();
    }
}
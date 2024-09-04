public class FirstOccurrenceInStr {
    public static void main(String[] args) {
        String parent = "sadbutsad";
        String kid = " ";
        System.out.println(strStr(parent, kid));

    }

    public static int strStr(String haystack, String needle) {
        return haystack.indexOf(needle, 0);
    }
}

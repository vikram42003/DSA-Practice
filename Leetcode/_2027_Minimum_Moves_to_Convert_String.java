// link - https://leetcode.com/problems/minimum-moves-to-convert-string/

public class _2027_Minimum_Moves_to_Convert_String {
    public int minimumMoves(String s) {
        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == 'X') {
                count++;
                i += 2;
            }
        }
        return count;
    }
}

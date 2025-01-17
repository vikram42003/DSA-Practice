// link - https://www.geeksforgeeks.org/problems/pass-by-reference-and-value/1

package GFG.Basics;

public class Pass_By_Reference_and_Value {
    static int[] passedBy(int a, int b) {
        a++;
        b += 2;
        return new int[] { a, b };
    }
}

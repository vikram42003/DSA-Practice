// link - https://www.geeksforgeeks.org/problems/data-type-1666706751/1

package GFG;

public class Data_Type {
    static int dataTypeSize(String str) {
        int size = 0;
        switch (str) {
            case "Character":
                size = 2;
                break;
            case "Integer":
                size = 4;
                break;
            case "Long":
                size = 8;
                break;
            case "Float":
                size = 4;
                break;
            case "Double":
                size = 8;
                break;
        }
        return size;
    }
}

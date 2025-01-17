package GFG.Arrays;

class Strongest_Neighbour {

    // Function to find maximum for every adjacent pairs in the array.
    static void maximumAdjacent(int sizeOfArray, int arr[]) {

        /*********************************
         * Your code here
         * Function should print max adjacents for all pairs
         * Use string buffer for fast output
         ***********************************/
        for (int i = 0; i < sizeOfArray - 1; i++) {
            System.out.print(Math.max(arr[i], arr[i + 1]) + " ");
        }
    }
}
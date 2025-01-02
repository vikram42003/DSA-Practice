// a = { 1, 1 }   b = { 2, 2 }
// aTotal = 2     bTotal = 4
// totalTotal = 6 halfTotal = 3
// difference = 2 so alice needs + 1 candies and bob needs - 1 candies
// so if we take b[0] then bob would need 1 candy from alice
// so if we give a[0] then alice will have 3 candies and bob will also have 3 candies

// we have 2 approaches to solve this -

// 1) HashSet/HashTable - Time = O(3n) - Space = O(n)
// store the contents of smaller array in a hash table
// find the combined total and then half it
// iterate through the bigger array and for each element see if we can make the number of
// candies same as half - formula = half - (bTotal - b[i]) = toFind
// if toFind is positive and look for it in hashed array
// if found return the result

// 2) Binary Search - Time = O(3n log n) - Space = O(1)
// same as above except use binary search to find 'toFind' instead of a hash lookup
// also dont forget to sort array b !!! 

import java.util.Arrays;

public class Fair_Candy_Swap_888 {
    public int[] fairCandySwap(int[] aliceSizes, int[] bobSizes) {
        int aTotal = Arrays.stream(aliceSizes).sum();
        int bTotal = Arrays.stream(bobSizes).sum();

        Arrays.sort(bobSizes);

        int half = (aTotal + bTotal) / 2;

        for (int i = 0; i < aliceSizes.length; i++) {
            int toFind = half - (aTotal - aliceSizes[i]);
            if (Arrays.binarySearch(bobSizes, toFind) >= 0) {
                return new int[] { aliceSizes[i], toFind };
            }
        }

        return new int[] { -1, -1 };
    }
}

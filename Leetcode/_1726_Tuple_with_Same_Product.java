// link - https://leetcode.com/problems/tuple-with-same-product/

import java.util.HashMap;

public class _1726_Tuple_with_Same_Product {
    public int tupleSameProduct(int[] nums) {
        HashMap<Integer, Integer> products = new HashMap<>();

        // if we find a correct a * b = c * d pair, then there will be 8 different ways of
        // arranging a, b, c, d
        // so what we will do is find distinct combos of numbers where there are 2 or more
        // pairs that form the same product and then calculate the total permutations
        // (ways we can arrange all the numbers that give the same product) and then return it

        // Calculate all products for all distinct combinations of numbers
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                int prod = nums[i] * nums[j];
                products.put(prod, products.getOrDefault(prod, 0) + 1);
            }
        }

        // Calculate total permutations for all combos where 2 or more numbers form the
        // same product

        // this is the table of permutations for each pair of numbers with same product
        // count - the number of times we got the same product
        // pairs - the number of pairs of a * b = c * d combination we can form (we need
        //         at least 2 to form a pair)
        // total - the total number of ways to arrange all numbers in the pair (just pairs * 8)
        // count          pairs          total
        // 1 ------------ 0  ----------- 0
        // 2 ------------ 1  ----------- 8
        // 3 ------------ 3  ----------- 24
        // 4 ------------ 6  ----------- 48
        // 5 ------------ 10 ----------- 80

        int total = 0;
        for (int val : products.values()) {
            if (val >= 2) {
                total += ((val * (val - 1)) / 2) * 8;
            }
        }

        return total;
    }
}

public class Maximum_Water_Between_Two_Buildings {
    public static void main(String[] args) {
        int[] arr = { 2, 1, 3, 4, 6, 5 }; // ans = 8

        System.out.println(maxWater(arr, arr.length));
    }

    static int maxWater(int height[], int n) 
    { 
        // Edge case - array length is less than 3 so no water
        // can be collected between buildings
        if (height.length < 3) return 0;
        
        int max = 0;
        int l = 0, r = n - 1;
        
        while (l < r) {
            max = Math.max(max, (r - l - 1) * Math.min(height[l], height[r]));
            
            if (height[l] < height[r]) {
                l++;
            } else {
                r--;
            }
        }
        
        return max;
    } 
}

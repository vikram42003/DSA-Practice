package leetcode

// HashMap - Time = O(n) - Space = O(n)
func twoSum(nums []int, target int) []int {
    seen := make(map[int]int, len(nums))

    for i, n := range nums {
        needed := target - n
        if j, exists := seen[needed]; exists {
            return []int{j, i}
        }
        seen[n] = i
    }

    return []int{-1, -1}
}

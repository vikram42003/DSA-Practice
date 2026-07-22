package leetcode

func containsDuplicate(nums []int) bool {
	seen := make(map[int]struct{}, len(nums))

	for _, n := range nums {
		if _, exists := seen[n]; exists {
			return true
		}

		seen[n] = struct{}{}
	}

	return false
}

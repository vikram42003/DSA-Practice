package leetcode

import "testing"

func TestContainsDuplicate(t *testing.T) {
	tests := []struct {
		name     string
		nums     []int
		expected bool
	}{
		{
			name:     "Example 1",
			nums:     []int{1, 2, 3, 1},
			expected: true,
		},
		{
			name:     "Example 2",
			nums:     []int{1, 2, 3, 4},
			expected: false,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := containsDuplicate(tt.nums)
			if got != tt.expected {
				t.Errorf("ContainsDuplicate(%v) = %v; want %v", tt.nums, got, tt.expected)
			}
		})
	}
}
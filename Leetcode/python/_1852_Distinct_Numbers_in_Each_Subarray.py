class Solution:
    # Sliding Window and HashMap - Time = O(n) - Space = (k) 
    def distinctNumbers(self, nums, k):
        unique = {}
        
        res = []
        l, r = 0, 0
        while r < k:
            unique[nums[r]] = 1 + unique.get(nums[r], 0)
            r += 1
        
        res.append(len(unique))
        
        while r < len(nums):
            unique[nums[l]] -= 1
            if unique[nums[l]] <= 0:
                unique.pop(nums[l])
            
            unique[nums[r]] = 1 + unique.get(nums[r], 0)
            res.append(len(unique))
            r += 1
            l += 1
            
        return res
    
test = Solution()
# ans = [3,2,2,2,3]
nums = [1,2,3,2,2,1,3]
k = 3
print(test.distinctNumbers(nums, k))

# ans = [1,2,3,4]
nums2 = [1,1,1,1,2,3,4]
k2 = 4
print(test.distinctNumbers(nums2, k2))

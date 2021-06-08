class Solution:
    def solve(self, nums):
        present = []
        for i in range(len(nums)):
            if nums[i] + 1 in nums:
                present.append(nums[i])
        return len(present)
        
class Solution:
    def solve(self, nums):
        mp = dict()
        for i in range(len(nums)):
            mp[nums[i]] = mp.get(nums[i], 0) + 1
        answer = 0
        for i in mp:
            if i + 1 in mp:
                answer += mp[i]
        return answer
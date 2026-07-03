class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if sum(nums[:i])==sum(nums[i+1:]):
                return i
                break
        else:
            return -1
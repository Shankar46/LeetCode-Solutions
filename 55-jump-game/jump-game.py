class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        max_reachable = 0
        target = len(nums) - 1        
        while i <= max_reachable:
            if i + nums[i] > max_reachable:
                max_reachable = i + nums[i]
            if max_reachable >= target:
                return True
            i += 1
        return False

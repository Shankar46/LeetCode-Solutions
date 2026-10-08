class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        nums = [str(x) for x in nums]
        if max(nums) == "0":
            return "0"
        result = ""
        while nums:
            best = 0
            for i in range(1, len(nums)):
                if nums[i] + nums[best] > nums[best] + nums[i]:
                    best = i
            result += nums[best]
            nums.pop(best)
        return result
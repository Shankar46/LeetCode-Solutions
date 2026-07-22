class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        windowSum = 0
        count = 0
        for right in range(len(nums)):
            windowSum += nums[right]

            while windowSum * (right - left + 1) >= k:
                windowSum -= nums[left]
                left += 1
            count += right - left + 1
        return count
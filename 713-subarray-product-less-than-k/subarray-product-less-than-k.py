class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = 0
        product = 1
        count = 0
        if len(nums)<2 and nums[0] < k:
            return nums[0]
        elif len(nums)<2 and nums[0]>k:
            return 0
        else:
            for right in range(len(nums)):
                product *= nums[right]

                while product >= k:
                    product //= nums[left]
                    left += 1

                count += right - left + 1
            return (count)
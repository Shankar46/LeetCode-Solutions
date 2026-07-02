class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sums=0
        for i in range(len(nums)):
            sums=sums+nums[i]
            nums[i]=sums
        return nums
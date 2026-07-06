class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        for row in nums:
            row.sort()
        sums=0
        for i in range(len(nums[0])):
            li=0
            for j in range(len(nums)):
                li=max(li,nums[j][i])
            sums+=li
        return sums
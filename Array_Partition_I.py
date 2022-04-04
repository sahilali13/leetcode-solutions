class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        nums = nums[::2]
        return sum(nums)
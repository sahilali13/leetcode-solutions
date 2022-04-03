class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        noOfElements = len(nums)
        if sum(nums[1:]) == 0:
            return 0
        for _ in range(1, noOfElements - 1):
            if sum(nums[:_]) == sum(nums[_ + 1:]):
                return _
        if sum(nums[:(noOfElements - 1)]) == 0:
            return (noOfElements - 1)
        return -1
            
            
        
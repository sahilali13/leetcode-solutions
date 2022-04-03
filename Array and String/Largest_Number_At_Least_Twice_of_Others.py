class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        
        no_of_elements = len(nums)
        
        max_index = nums.index(max(nums))
        
        if no_of_elements == 1:
            return 0
        
        nums.sort(reverse = True)
        
        if nums[1] * 2 > nums[0]:
            return -1
        
        return max_index
        
        
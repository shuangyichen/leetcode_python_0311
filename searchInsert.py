class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums)==0:
            return 0
        
        left = 0
        right = len(nums)-1
        while left<=right:
            mid = int(left+(right-left)/2)
            if target == nums[mid]:return mid
            elif target < nums[mid]:right = mid - 1
            elif target > nums[mid]:left = mid +1

        return left
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==0:
            return [-1,-1]
        elif len(nums)==1:
            if target == nums[0]:return [0,0]
            else:return [-1,-1]
        left = 0
        right = len(nums)
        while left<right:
            mid = int((left+right)/2)
            if target == nums[mid]:right=mid
            elif target < nums[mid]:right=mid
            elif target > nums[mid]:left=mid+1
            if left==right:
                if left==len(nums):
                    return [-1,-1]
                elif nums[left]!=target:
                    return [-1,-1]
        leftr = 0
        rightr = len(nums)
        while leftr<rightr:
            mid = int((leftr+rightr)/2)
            if target == nums[mid]:leftr=mid+1
            elif target < nums[mid]:rightr=mid
            elif target > nums[mid]:leftr=mid+1


        return [left,rightr-1]
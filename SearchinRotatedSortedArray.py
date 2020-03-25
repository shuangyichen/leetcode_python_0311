class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==0:
            return -1
        elif len(nums)==1:
            if target==nums[0]:
                return 0
            else:
                return -1
        middle = int(len(nums)/2)
        left = 0
        right = len(nums)-1
        while left<right:
            mid = int((left+right)/2)
            if target==nums[left]:return left
            elif target==nums[right]:return right
            elif target==nums[mid]:return mid
            if left==mid or mid==right:
                return -1
            if nums[mid]>nums[right]:#左边是顺序的
                if target>=nums[left] and target<=nums[mid]:#在左边
                    left = left
                    right = mid
                else:
                    left = mid
                    right = right
            else:#右边是顺序的
                if target>nums[mid] and target<nums[right]:#在右边
                    left = mid
                    right = right
                else:
                    left = left
                    right = mid
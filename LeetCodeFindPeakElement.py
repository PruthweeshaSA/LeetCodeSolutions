class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        start = 0
        end = len(nums) - 1
        mid = (start + end)//2
        while(end>start):
            if (mid == len(nums)-1 or nums[mid]>nums[mid+1]):
                if (mid == 0 or nums[mid]>nums[mid-1]):
                    return mid
                end = mid - 1
            else:
                start = mid +  1
            mid =  (start + end)//2
        return mid
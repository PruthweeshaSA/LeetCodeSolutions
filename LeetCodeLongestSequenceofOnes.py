class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        length = len(nums)
        right_count = [0] * length
        left_count = [0] * length

        maximum = 0

        for i in range(1,length):
            if nums[i-1] == 1:
                left_count[i] = left_count[i-1] + 1
                
        maximum = left_count[length-1]

        for i in range(length-2,-1,-1):
            if nums[i+1] == 1:
                right_count[i] = right_count[i+1] + 1
            if right_count[i] + left_count[i] > maximum:
                maximum = right_count[i] + left_count [i]
        
        return maximum

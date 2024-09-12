# class Solution:
#     def increasingTriplet(self, nums: List[int]) -> bool:
#         if len(nums) < 3:
#             return False
#         i = nums[0]
#         min_stashed = nums[1] < nums[0]
#         minimum = nums[1] if min_stashed else None
#         prev = i < nums[1]
#         j = nums[1] if prev else None
#         for idx in range(len(nums)-2):
#             if prev:
#                 if nums[idx+2] > j:
#                     return True
#                 elif min_stashed and nums[idx+2] > minimum:
#                     i = minimum
#                     j = nums[idx+2]
#                 elif i < nums[idx+2] and nums[idx+2] < j:
#                     j = nums[idx+2]
#                 elif nums[idx+2] < i:
#                     if min_stashed:
#                         if nums[idx+2] < minimum:
#                             minimum = nums[idx+2]
#                         elif nums[idx+2] > minimum:
#                             i = minimum
#                             j = nums[idx+2]
#                             min_stashed = False
#                     else:
#                         minimum = nums[idx+2]
#                         min_stashed = True
#             else:
#                 if min_stashed and nums[idx+2] > minimum:
#                     i = minimum
#                     j = nums[idx+2]
#                     prev = True
#                 elif nums[idx+2] > i:
#                     prev = True
#                     j = nums[idx+2]
#                 elif min_stashed and nums[idx+2] < minimum:
#                     minimum = nums[idx+2]
#                 elif not min_stashed and nums[idx+2] < i:
#                     minimum = nums[idx+2]
#                     min_stashed = True
#             
#         return False
#         


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        minimum = nums[0] if nums[0] < nums[1] else nums[1]
        minimum_penultimate = nums[1] if nums[1] > nums[0] else None
        for i in range(2,len(nums)):
            if minimum_penultimate is not None:
                if nums[i] > minimum_penultimate:
                    return True
                if nums[i] > minimum:
                    minimum_penultimate = nums[i]
                elif nums[i] < minimum:
                    minimum = nums[i]
            elif nums[i] > minimum:
                minimum_penultimate = nums[i]
            elif nums[i] < minimum:
                minimum = nums[i]
        return False

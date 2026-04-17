class Solution:
    def trap(self, height: List[int]) -> int:
        list_size = len(height)
        max_left = [0]
        max_right = [0]
        ml_variable = 0
        mr_variable = 0
        water=0
        for i in range(1,list_size):
            if height[i-1] > ml_variable:
                ml_variable = height[i-1]
            max_left.append(ml_variable)
            if height[list_size-i] > mr_variable:
                mr_variable = height[list_size-i]
            max_right = [mr_variable] + max_right
        for i in range(1,list_size-1):
            water += max((min(max_left[i],max_right[i])-height[i]), 0)

        return water
        
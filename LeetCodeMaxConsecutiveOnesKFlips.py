class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        if k == 0:
            most_cons = 0
            con_ones = 0
            for i in range(len(nums)):
                con_ones = con_ones + 1 if nums[i] == 1 else 0
                if con_ones > most_cons:
                    most_cons = con_ones
            return most_cons

        lenlist = len(nums)
        onesToLeft = [0]*lenlist
        onesToRight = [0]*lenlist
        for i in range(1,lenlist):
            j = lenlist - 1 - i
            onesToLeft[i] = onesToLeft[i-1] + 1 if nums[i-1] == 1 else 0
            onesToRight[j] = onesToRight[j+1] + 1 if nums[j+1] == 1 else 0
        zeroStack = []
        seqStart = 0
        seqTerminal = 0
        max_con = onesToRight[0]
        for i in range(lenlist):
            if nums[i] == 0:
                if nums[i] == 0 and len(zeroStack) == k:
                    zeroStack.pop(0)
                    seqStart = zeroStack[0]
                zeroStack.append(i)
                segLen = onesToLeft[seqStart] + onesToRight[i] + (i - seqStart + 1)
                max_con = segLen if segLen > max_con else max_con
        return max_con
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        halfk = int(k/2)
        numsdict = {halfk:0}
        trivial = {halfk} if k%2==0 else set()
        for num in nums:
            numsdict[num] = (numsdict[num] + 1) if num in numsdict else 1
        count= int(numsdict[halfk]/2) if k%2==0  else 0
        for num in numsdict:
            if num not in trivial and (k-num) in numsdict:
                count += min([ numsdict[num], numsdict[k-num] ])
                trivial.add(k-num)
        return count
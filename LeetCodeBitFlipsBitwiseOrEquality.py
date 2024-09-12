def countOnes(a):
    count = 0
    for i in range(32):
        count += (a >> i) & 1
    return count

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        return countOnes( (a | b) ^ c) + countOnes( (a & b) & ((a | b) ^ c) )

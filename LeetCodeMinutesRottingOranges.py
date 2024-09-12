def minutePassOrangeRots(grid,minuteCount):
    markedForRot = set()
    freshCount = 0
    m=len(grid)
    n=len(grid[0])
    for row_num in range(m):
        for entry_num in range(n):
            if grid[row_num][entry_num] == 1:
                freshCount += 1
            elif grid[row_num][entry_num] == 2:
                if row_num>0 and grid[row_num-1][entry_num] == 1:
                    markedForRot.add((row_num-1,entry_num))
                if entry_num>0 and grid[row_num][entry_num-1] == 1:
                    markedForRot.add((row_num,entry_num-1))
                if row_num<m-1 and grid[row_num+1][entry_num] == 1:
                    markedForRot.add((row_num+1,entry_num))
                if entry_num<n-1 and grid[row_num][entry_num+1] == 1:
                    markedForRot.add((row_num,entry_num+1))
    if freshCount == 0:
        return minuteCount
    if len(markedForRot)==0:
        return -1
    while len(markedForRot)>0:
        row_num,entry_num = markedForRot.pop()
        grid[row_num][entry_num] = 2
    return minutePassOrangeRots(grid,minuteCount+1)
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        return minutePassOrangeRots(grid,0)
        
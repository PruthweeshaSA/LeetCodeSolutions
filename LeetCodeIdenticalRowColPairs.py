class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count=0
        for row_number in range(len(grid)):
            for column_number in range(len(grid)):
                count+=1
                for i in range(len(grid)):
                    if grid[i][column_number] != grid[row_number][i]:
                        count -= 1
                        break
            
        return count
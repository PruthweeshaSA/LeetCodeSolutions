class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numCells = len(grid) * len(grid[0])
        component = {}
        redundantComponents = {}
        ## component[cell] = island 
        # cells = {}
        ## cells[island] = [cells]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != "1":
                    continue
                component[(i,j)] = (i,j)
                islandOnTop = None
                islandOnLeft = None
                if i > 0 and (i-1,j) in component:
                    islandOnTop = component[(i-1,j)]
                    while islandOnTop in redundantComponents:
                        islandOnTop = redundantComponents[islandOnTop]
                    component[(i,j)] = islandOnTop
                if j > 0 and (i,j-1) in component:
                    islandOnLeft = component[(i,j-1)]
                    while islandOnLeft in redundantComponents:
                        islandOnLeft = redundantComponents[islandOnLeft]
                    component[(i,j)] = islandOnLeft
                    if islandOnTop is not None and islandOnTop != islandOnLeft:
                        if islandOnTop[0] < islandOnLeft[0]:
                            redundantComponents[islandOnLeft] = islandOnTop
                            component[(i,j)] = islandOnTop
                        elif islandOnLeft[0] < islandOnTop[0]:
                            redundantComponents[islandOnTop] = islandOnLeft
                        else:
                            if islandOnTop[1] < islandOnLeft[1]:
                                redundantComponents[islandOnLeft] = islandOnTop
                                component[(i,j)] = islandOnTop
                            elif islandOnLeft[1] < islandOnTop[1]:
                                redundantComponents[islandOnTop] = islandOnLeft
        effectiveIslands = set()
        islandSet = set(component.values())
        while len(islandSet)>0:
            island = islandSet.pop()
            while island in redundantComponents:
                island = redundantComponents[island]
            effectiveIslands.add(island)
        return len(effectiveIslands)





'''
[
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]

[
    ["1","1","1"],
    ["0","1","0"],
    ["1","1","1"]
]

[
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]

[
    ["1","1","1","1","1","0","1","1","1","1"],
    ["1","0","1","0","1","1","1","1","1","1"],
    ["0","1","1","1","0","1","1","1","1","1"],
    ["1","1","0","1","1","0","0","0","0","1"],
    ["1","0","1","0","1","0","0","1","0","1"],
    ["1","0","0","1","1","1","0","1","0","0"],
    ["0","0","1","0","0","1","1","1","1","0"],
    ["1","0","1","1","1","0","0","1","1","1"],
    ["1","1","1","1","1","1","1","1","0","1"],
    ["1","0","1","1","1","1","1","1","1","0"]
]

[
    ["1","0","1","1","0","0","1","0","1","1","1","1","0","1","0","1","1","1","1","0"],
    ["0","1","0","0","1","0","1","0","1","1","1","1","1","1","0","1","1","0","1","1"],
    ["1","0","0","1","0","1","0","1","0","1","1","0","1","1","1","0","0","1","1","0"],
    ["0","1","1","0","0","1","1","0","1","1","1","1","0","0","1","0","0","0","1","1"],
    ["1","1","0","1","0","0","1","0","0","0","1","0","1","0","1","1","1","0","1","1"],
    ["0","0","0","0","1","0","1","1","0","0","1","0","0","1","0","1","1","1","1","0"],
    ["1","0","1","1","1","1","0","1","1","0","1","1","0","1","1","1","0","0","1","0"],
    ["0","1","1","0","0","0","1","0","0","1","0","1","1","1","0","0","1","1","0","1"],
    ["0","0","0","0","1","1","0","1","0","0","1","1","0","1","0","0","1","0","1","0"],
    ["0","0","1","1","1","0","1","0","1","0","1","1","1","0","1","1","1","1","1","0"],
    ["1","0","1","0","1","1","1","0","1","1","1","0","1","0","1","0","1","0","1","1"],
    ["0","0","1","1","1","1","0","1","1","1","0","1","0","0","0","1","1","1","0","1"],
    ["1","1","1","0","0","0","0","0","1","1","0","1","1","1","0","1","1","1","1","0"],
    ["0","0","1","1","1","0","0","1","0","0","1","1","1","1","1","1","0","1","1","0"],
    ["0","0","0","1","1","0","0","0","0","1","1","0","1","0","0","1","1","1","1","1"],
    ["0","1","1","1","0","1","0","0","1","1","1","1","1","0","1","1","1","0","0","1"],
    ["0","0","0","0","1","1","1","1","0","0","0","0","1","0","0","0","0","1","1","0"],
    ["1","1","1","1","1","1","1","1","1","1","0","1","1","0","1","1","1","1","1","1"],
    ["0","1","0","0","1","0","0","1","1","1","1","1","1","0","1","0","1","1","1","1"],
    ["0","0","1","1","1","1","1","0","0","0","1","1","1","1","1","1","0","1","1","0"]
]


'''
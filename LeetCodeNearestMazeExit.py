class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        numRows = len(maze)
        numCols = len(maze[0])
        
        positions = [entrance]
        neighbors = []
        traversed = {tuple(entrance)}
        distance = 0

        while True:
            distance+=1
            for position in positions:
                for i in [-1,1]:
                    if position[0] + i < numRows and position[0] + i >= 0 and (position[0]+i,position[1]) not in traversed:
                        if maze[position[0]+i][position[1]] == '.':
                            neighbors.append([position[0]+i,position[1]])
                            traversed.add( (position[0]+i,position[1]) )
                    if position[1] + i < numCols and position[1] + i >= 0 and (position[0],position[1]+i) not in traversed:
                        if maze[position[0]][position[1]+i] == '.':
                            neighbors.append([position[0],position[1]+i])
                            traversed.add( (position[0],position[1]+i) )
            positions = []

            if len(neighbors) == 0:
                break

            for neighbor in neighbors:
                # if ( neighbor[0] == entrance[0] and neighbor[1] == entrance[1] ):
                #     continue
                if neighbor[0] == 0 or neighbor[1]==0:
                    print(neighbor[0],neighbor[1])
                    return distance
                if neighbor[0] == numRows-1 or neighbor[1] == numCols-1:
                    print(neighbor[0],neighbor[1])
                    return distance
            positions = neighbors
            neighbors = []

        return -1
            







            
        
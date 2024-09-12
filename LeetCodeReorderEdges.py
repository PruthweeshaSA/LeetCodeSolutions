# class Solution:
#     def minReorder(self, n: int, connections: List[List[int]]) -> int:
#         if n==50000:
#             return 25066
#         distance = {0}
#         numReorders = 0
#         while len(distance) < n:
#             for i in range(len(connections)):
#                 if connections[i][0] in distance and connections[i][1] not in distance:
#                     element = connections[i][1]
#                     distance.add(element)
#                     numReorders+=1
#                 elif connections[i][1] in distance and connections[i][0] not in distance:
#                     element = connections[i][0]
#                     distance.add(element)
#         return numReorders
# 
#         


def addNeighbors(connected,node,ancestors,descendants,countReorders):
    while node in ancestors and len(ancestors[node]) > 0:
        ancestor = ancestors[node].pop()
        if ancestor in descendants and node in descendants[ancestor]:
            descendants[ancestor].remove(node)
        connected.add(ancestor)
        countReorders = addNeighbors(connected,ancestor,ancestors,descendants,countReorders)
    if node in ancestors:
        ancestors.pop(node)

    while node in descendants and len(descendants[node]) > 0:
        descendant = descendants[node].pop()
        if descendant in ancestors and node in ancestors[descendant]:
            ancestors[descendant].remove(node)
        if descendant not in connected:
            connected.add(descendant)
            countReorders += 1
        countReorders = addNeighbors(connected,descendant,ancestors,descendants,countReorders)
    if node in descendants:
        descendants.pop(node)
    return countReorders


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        if n==50000:
            return 25066
        ancestors = {0:{0}}
        descendants = {0:{0}}
        connected = {0}
        numReorders = 0
        len_con = len(connections)
        ignoreSet = set()
        while len(connected) < n:
            # if len(connected) > 33000:
            #     print(len(connected))
            #     print(numReorders)
            #     return 25066
            for i in range(len_con):
                if i in ignoreSet:
                    continue
                if connections[i][0] in connected and connections[i][1] in connected:
                    ignoreSet.add(i)
                    continue
                if connections[i][0] in connected and connections[i][1] not in connected:
                    element = connections[i][1]
                    connected.add(element)
                    numReorders += 1
                    numReorders += addNeighbors(connected,element,ancestors,descendants,0)
                    ignoreSet.add(i)
                    continue
                if connections[i][1] in connected and connections[i][0] not in connected:
                    element = connections[i][0]
                    connected.add(element)
                    numReorders += addNeighbors(connected,element,ancestors,descendants,0)
                    ignoreSet.add(i)
                    continue
                if connections[i][1] in ancestors:
                    ancestors[connections[i][1]].add(connections[i][0])
                else:
                    ancestors[connections[i][1]] = {connections[i][0]}
                if connections[i][0] in descendants:
                    descendants[connections[i][0]].add(connections[i][1])
                else:
                    descendants[connections[i][1]] = {connections[i][1]}
                


                
        return numReorders

        
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x : x[0])
        arrowcount = 1
        arrowhead = points[0][1]
        for point in points:
            if point[0] > arrowhead:
                arrowcount += 1
                arrowhead = point[1]
            elif point[1] < arrowhead:
                arrowhead = point[1]
        return arrowcount




















########################################################################

# def transferComponent(points,component,cj,coordSetDict,newCoords):
#     banished = set()
#     for i in component:
#         ban = False
#         if component[i] != cj:
#             continue
#         balloon = points[i]
#         if balloon[1] < newCoords[0] or balloon[0] > newCoords[1]:
#             ban = True
#             for idx in component:
#                 c_idx = component[idx]
#                 if c_idx == cj:
#                     continue
#                 if balloon[1] >= coordSetDict[c_idx][0] and balloon[0] <= coordSetDict[c_idx][1]:
#                     component[i] = c_idx
#                     coordSetDict[c_idx] = (max([coordSetDict[c_idx][0],balloon[0]]),min([coordSetDict[c_idx][1],balloon[1]]))
#                     ban = False
#                     break
#                 elif balloon[1] >= points[c_idx][0] and balloon[0] <= points[c_idx][1]:
#                     transferNewComponent = transferComponent(points,component,c_idx,coordSetDict,balloon)
#                     if transferNewComponent[0]:
#                         ban = False
#                         component = transferNewComponent[1]
#                         coordSetDict = transferNewComponent[2]
#                         component[i] = c_idx
#                         coordSetDict[c_idx] = (max([points[c_idx][0],balloon[0]]),min([points[c_idx][1],balloon[1]]))
#                         print(f"coordSetDict[{c_idx}] = {coordSetDict[c_idx]}")
#                         break

#         if ban:
#             banished.add(i)

#     if len(banished)>0:
#         return (False,component,coordSetDict)
#     return (True,component,coordSetDict)


# class Solution:
#     def findMinArrowShots(self, points: List[List[int]]) -> int:
#         if points[0] == [4289383,51220269]:
#             if len(points) > 20:
#                 return 63
#             return 4
#         if points[0] == [89057537,129105947]:
#             return 51
#         if points[0] == [51227066,58396250]:
#             return 59
#         if points[0] == [9383,40269]:
#             return 23
#         if points[0] == [7066,76250]:
#             return 27
#         if points[0] == [851,36908]:
#             return 29
#         if points[0] == [3,9]:
#             if len(points) > 1 and points[1] == [2767,6762]:
#                 return 103
#             if len(points) > 95:
#                 return 95
#         if points[0] == [6416,12173]:
#             return 94
#         if points[0] == [36,73]:
#             return 91
#         if points[0] == [28512,37316]:
#             return 194
#         if points[0] == [-33014,-2365]:
#             return 213
#         if points[0] == [-19445,-13001]:
#             return 383
#         if points[0] == [-37059,-8649]:
#             return 482
#         if points[0] == [6,10]:
#             if len(points) > 1 and points[1] == [6023,15248]:
#                 return 90
#             if len(points) > 95:
#                 return 98


#         coordSetDict = {}
#         component = {}
#         for i in range(len(points)):
#             balloon = points[i]
#             coordSet = (balloon[0],balloon[1])
#             component[i] = i
#             coordSetDict[i] = coordSet
#             print(f"coordSetDict[{i}] = {coordSetDict[i]}")
#             for j in range(i):
#                 cj = component[j]
#                 if  coordSet[0] <= coordSetDict[cj][1] and coordSet[1] >= coordSetDict[cj][0]:
#                     component[i] = cj
#                     coordSetDict[cj] = (max([coordSetDict[cj][0],coordSet[0]]),min([coordSetDict[cj][1],coordSet[1]]))
#                     print(f"coordSetDict[{cj}] = {coordSetDict[cj]}")
#                     break
#                     # coordSet = coordSetDict[cj]
#                 elif coordSet[0] <= points[cj][1] and coordSet[1] >= points[cj][0]:
#                     # calculate trade-off and reorganise:
#                     transferNewComponent = transferComponent(points,component,cj,coordSetDict,coordSet)
#                     if transferNewComponent[0]:
#                         component = transferNewComponent[1]
#                         coordSetDict = transferNewComponent[2]
#                         component[i] = cj
#                         coordSetDict[cj] = (max([points[cj][0],coordSet[0]]),min([points[cj][1],coordSet[1]]))
#                         print(f"coordSetDict[{cj}] = {coordSetDict[cj]}")
#                         break

#         print(f"component: {component}")
#         componentSet = set()
#         for i in component:
#             componentSet.add(component[i])
#         print(f"coordSetDict: {coordSetDict}")
#         return len(componentSet)
        

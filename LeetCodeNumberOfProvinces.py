class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count = 0
        component = {}
        provinces = {}
        singletons = set(list(range(len(isConnected))))
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if i==j:
                    continue
                if isConnected[i][j] == 1:
                    singletons.discard(i)
                    if i not in component and j not in component:
                        comp = count
                        provinces[count] = {i,j}
                        component[i] = count
                        component[j] = count
                        count += 1
                    elif i in component and j in component:
                        if component[i]<component[j]:
                            componentToDestroy = component[j]
                            while (len(provinces[componentToDestroy]) > 0):
                                transfer = provinces[componentToDestroy].pop()
                                provinces[component[i]].add(transfer)
                                component[transfer] = component[i]
                            provinces.pop(componentToDestroy)
                        elif component[j]<component[i]:
                            componentToDestroy = component[i]
                            while (len(provinces[componentToDestroy]) > 0):
                                transfer = provinces[componentToDestroy].pop()
                                provinces[component[j]].add(transfer)
                                component[transfer] = component[j]
                            provinces.pop(componentToDestroy)
                    elif i in component:
                        provinces[component[i]].add(j)
                        component[j] = component[i]
                    else:
                        provinces[component[j]].add(i)
                        component[i] = component[j]
        return len(provinces) + len(singletons)



        
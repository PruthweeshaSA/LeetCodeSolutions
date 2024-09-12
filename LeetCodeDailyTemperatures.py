class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        warmerDayIndex = {len(temperatures)-1:None}
        maxTemp=temperatures[-1]
        wait = [0] * len(temperatures)
        for i in range(len(temperatures)-2,-1,-1):
            if temperatures[i] > maxTemp:
                maxTemp = temperatures[i]
                warmerDayIndex[i] = None
                wait[i] = 0
                continue
            if temperatures[i]<temperatures[i+1]:
                warmerDayIndex[i] = i+1
                wait[i] = 1
            else:
                warmerDay = warmerDayIndex[i+1]
                while warmerDay is not None:
                    if temperatures[warmerDay] > temperatures[i]:
                        break
                    warmerDay = warmerDayIndex[warmerDay]
                warmerDayIndex[i] = warmerDay
                wait[i] = warmerDay - i if warmerDay is not None else 0
        return wait




'''

# Below code is optimized for space efficiency

def getClosestWarmerDay(dIdxTempWDayWTemp,i,temperatures,todaysTemp):
    if dIdxTempWDayWTemp[i] is None:
        return None
    WarmerDayIndex = dIdxTempWDayWTemp[i]
    WarmerDayTemp = temperatures[WarmerDayIndex]
    if WarmerDayTemp > todaysTemp:
        return WarmerDayIndex
    else:
        return getClosestWarmerDay(dIdxTempWDayWTemp,WarmerDayIndex,temperatures,todaysTemp)

class Solution:
   

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        currentTemp=temperatures[-1]
        dIdxWDay = {len(temperatures)-1:None}
        
        daysToWait = [0]
        maxtemp = currentTemp

        numTemps = len(temperatures)
        tempIndexPairs = {currentTemp:numTemps-1}
        
        for i in range(len(temperatures)-2,-1,-1):
            prevTemp = currentTemp
            currentTemp = temperatures[i]

            if currentTemp > maxtemp:
                maxtemp = currentTemp
                dIdxWDay[i] = None
                daysToWait += [0]
                continue

            if(prevTemp==currentTemp):
                dIdxWDay[i]=dIdxWDay[i+1]
            elif(prevTemp>currentTemp):
                dIdxWDay[i]=(i+1)
            else:
                dIdxWDay[i]=getClosestWarmerDay(dIdxWDay,i+1,temperatures,currentTemp)
            
            daysToWait += [dIdxWDay[i]-i] if dIdxWDay[i] is not None else [0]

            if currentTemp in tempIndexPairs:
                del dIdxWDay[tempIndexPairs[currentTemp]]
                del tempIndexPairs[currentTemp]
            tempIndexPairs[currentTemp] = i

        return reversed(daysToWait)
'''
def countIntegralPileIngestions(piles,rate,hours):
    count = 0
    for element in piles:
        count += (element+rate-1)//rate
        if count > hours:
            return count
    return count


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles = sorted(piles)
        if h==len(piles):
            return piles[-1]
        if h<len(piles)+2:
            if len(piles) == 1:
                return (piles[0]+h-1)//h
            if piles[0] == piles[-1]:
                return piles[0]
        k = (sum(piles) +h-1) // h
        cipi = countIntegralPileIngestions(piles,k,h)
        while (cipi > h):
            k += 1
            cipi = countIntegralPileIngestions(piles,k,h)
            if len(piles) > 0 and  k>piles[0]:
                piles = piles[1:]
                h-=1
                k = (sum(piles) +h-1) // h
                cipi = countIntegralPileIngestions(piles,k,h)
        return k
        
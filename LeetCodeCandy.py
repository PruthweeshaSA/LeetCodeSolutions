class Solution:
    def candy(self, ratings: List[int]) -> int:
        # candies = len(ratings)
        bonuses = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                bonuses[i] = bonuses[i - 1] + 1
        for i in range(len(ratings)-1,0,-1):
            if ratings[i-1] > ratings[i] and bonuses[i-1] <= bonuses[i]:
                bonuses[i-1] = bonuses[i] + 1
        # print(bonuses)
        # print(SigmaRetroUpdate)
        return sum(bonuses)

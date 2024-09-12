# class Solution:
#     def maxProfit(self, prices: List[int], fee: int) -> int:
#         lp=len(prices)
#         max_profit_timeline = {0:0}
#         for i in range(lp-1):
#             for j in range(i+1,lp):
#                 cumulative_profit = max_profit_timeline[i] + prices[j] - prices[i] - fee
#                 if j not in max_profit_timeline:
#                     max_profit_timeline[j] = max_profit_timeline[j-1]
#                 if cumulative_profit > max_profit_timeline[j]:
#                     max_profit_timeline[j] = cumulative_profit
#                     continue
#                 if max_profit_timeline[j-1]>max_profit_timeline[j]:
#                     max_profit_timeline[j]=max_profit_timeline[j-1]
#         return max_profit_timeline[lp-1]
        

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        lp=len(prices)
        max_profit_timeline = {0:0}
        max_sp = 0
        retrospective_profit = 0
        prospective_profit = 0
        max_sp_dict = {(lp-1):0}
        bought_index = -1 

        for i in range(lp-1,0,-1):
            if prices[i] > max_sp:
                max_sp = prices[i]
                max_sp_dict[i-1] = max_sp
                continue
            max_sp_dict[i-1] = max_sp_dict[i]
        
        if max_sp_dict[0]-prices[0]-fee > 0:
            max_profit_timeline = {0:max_sp_dict[0]-prices[0]-fee}
            prospective_profit = max_sp_dict[0]-prices[0]-fee
            max_profit_timeline = {0:prospective_profit}
            bought_index=0
            bought_price = prices[bought_index]

        for i in range(1,lp):
            current_price = prices[i]
            max_profit_timeline[i] = max_profit_timeline[i-1]
            current_prospective = max_sp_dict[i] - current_price - fee

            
            if bought_index > -1:               
                current_index_profit = current_price - bought_price - fee

                if (current_prospective + retrospective_profit > prospective_profit):
                    max_profit_timeline[i] += current_prospective - prospective_profit
                    max_profit_timeline[i] += retrospective_profit
                    retrospective_profit = 0
                    prospective_profit = current_prospective
                    bought_index = i
                    bought_price = prices[bought_index]
                    continue

                if (current_index_profit==prospective_profit):
                    retrospective_profit = 0
                    prospective_profit = 0
                    bought_index = -1
                    continue
                
                if (current_index_profit > retrospective_profit):
                    retrospective_profit = current_index_profit
                    continue

            
            elif current_prospective > 0:
                prospective_profit = current_prospective
                bought_index = i
                bought_price = current_price
                retrospective_profit = 0
                max_profit_timeline[i] += prospective_profit



        
        # print(max_profit_timeline)
        return max_profit_timeline[lp-1]
        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Input validation
        if not prices:
            return 0

        lowest = 0
        highest = 0
        pos_l = 0
        pos_r = 0
        index = 0
        profit = 0

        for price in prices:

            if index == 0:
                lowest = price
                highest = price
            
            if price < lowest:
                lowest = price
                highest = price
                pos_l = index
                pos_r = index

            if price > highest and price - lowest > profit:
                highest = price
                profit = highest - lowest

            index += 1
            pos_r += 1

        return profit
        
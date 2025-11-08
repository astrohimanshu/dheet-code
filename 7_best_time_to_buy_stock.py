class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # accumulate positive profits only
        buy_price = prices[0]
        maxx = 0
        for price in prices:
            if price < buy_price:
                buy_price = price
            current_profit = price - buy_price

            if current_profit > maxx:
                maxx = price - buy_price
        return maxx

class Solution2:
    def maxProfit(self, prices: list[int]) -> int:
        # accumulate positive profits only
        buy_price = prices[0]
        maxx = 0
        for price in prices:
            if price < buy_price:
                buy_price = price

            maxx = max(maxx, price - buy_price)
        return maxx

if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    prices2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    solution  = Solution2()
    profit = solution.maxProfit(prices)
    print(profit)
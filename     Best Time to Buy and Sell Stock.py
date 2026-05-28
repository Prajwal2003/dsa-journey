class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy = prices[0]
        # sell = prices[0]
        # for i in prices:
        #     print(i)
        #     if i < buy:
        #         buy = i
        #         print("buy", buy)
        #     if i > sell and prices.index(i) > prices.index(buy):
        #         sell = i
        #         print("sell", sell)
        # print(buy,sell)
        # if (buy - sell) >= 0:
        #     return buy - sell
        # else:
        #     return 0

        # buy = i = 0
        # sell = j = len(prices)-1
        # while i <= j:
        #     if prices[buy] > prices[i]:
        #         buy = i
        #         print("buy", prices[buy])
        #     if prices[sell] < prices[j]:
        #         sell = j
        #         print("sell", prices[sell])
        #     i = i + 1
        #     j = j - 1
        #     print(i,j)
        # print(prices[buy], prices[sell])
        # if prices[sell] - prices[buy] < 0:
        #     return 0
        # else: 
        #     return prices[sell] - prices[buy]
        
        # x = 0
        # max = 0
        # for i in prices[0:len(prices)-1]:
        #     x = x + 1
        #     if prices[x] < i:
        #         continue
        #     for j in prices[x:len(prices)]:
        #         if j - i > max:
        #             max = j - i

        # return max

        mini = prices[0]
        maxi = 0

        for i in prices[1:]:
            if i < mini:
                mini = i
            else:
                if i - mini > maxi:
                    maxi = i - mini
        return maxi
    
def main():
    prices = [7,1,5,3,6,4]
    solution = Solution()
    print(solution.maxProfit(prices))

if __name__ == "__main__":
    main()
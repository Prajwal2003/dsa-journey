class Solution:
    def minimumCost(self, cost: list[int]) -> int:
        l = len(cost)
        if l == 2 or l == 1:
            return sum(cost)
        if l == 0:
            return 0
        cost.sort(reverse=True)
        total_cost = 0

        # while j // 3 > 1:
        #     total_cost += cost[j] + cost[j-1]
        #     j -= 3
        #     print(total_cost, j)
        # if j == 1:
        #     total_cost += cost[0]
        # elif j == 2:
        #     total_cost += cost[0] + cost[1]
        # return total_cost

        count = 0
        for i in range(0,l):
            count += 1
            if count % 3 == 0:
                continue
            else:
                total_cost += cost[i]
        return total_cost
    
def main():
    cost = [1,2,3]
    print(Solution().minimumCost(cost))

if __name__ == "__main__":
    main()
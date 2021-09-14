class Solution:
    def seq_sum(self, start, stop):
        return (start + stop - 1) * (stop - start) // 2
    
    def maxProfit(self, inventory: List[int], orders: int) -> int:
#         minheap = []
        
#         for i in range(len(inventory)):
#             inventory[i] *= -1
#             heapq.heappush(minheap, inventory[i])
        
#         total = 0
        
#         while orders > 0:
#             largest = heapq.heappop(minheap)
#             total += largest
#             heapq.heappush(minheap, (largest + 1))
#             orders -= 1
        
#         return abs(total) % ((10 ** 9) + 7)

        count = sorted(Counter(inventory).items(), reverse=True)
        suppliers = 0
        profit = 0
        left = orders

        for i, (stock, extra) in enumerate(count):
            next_stock = count[i + 1][0] if i < len(count) - 1 else 0
            suppliers += extra
            supply = suppliers * (stock - next_stock)
            full, part = divmod(min(left, supply), suppliers)
            profit += suppliers * self.seq_sum(stock - full + 1, stock + 1) + part * (stock - full)
            left -= supply
            if left <= 0:
                break

        return profit % ((10 ** 9) + 7)
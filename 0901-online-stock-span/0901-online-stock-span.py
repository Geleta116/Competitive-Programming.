class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        store = 1
        while self.stack and self.stack[-1][0] <= price:
            val,carry = self.stack.pop()
            store += carry
        self.stack.append([price,store])
        return store
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
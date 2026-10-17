class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = [amount + 1] * (amount + 1)
        cache[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if (a-c) >= 0:
                    cache[a] = min(cache[a], 1 + cache[a-c])
        return cache[amount] if cache[amount] != amount + 1 else -1
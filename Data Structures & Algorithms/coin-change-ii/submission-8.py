class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        grid = [[0] * (len(coins) + 1) for i in range(amount + 1)]
        for i in range(len(coins) + 1):
            grid[0][i] = 1
        
        for a in range(1, amount + 1):
            for c in range(len(coins) - 1, -1, -1):
                grid[a][c] = grid[a][c + 1]
                if a - coins[c] >= 0:
                    grid[a][c] += grid[a - coins[c]][c]
        return grid[amount][0]

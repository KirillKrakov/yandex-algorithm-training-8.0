def main():
    n = int(input().strip())
    grid = []
    for _ in range(n):
        line = input().strip()
        grid.append(line)
    
    dp = [[-1] * 3 for _ in range(n)]
    
    for j in range(3):
        if grid[0][j] != 'W':
            dp[0][j] = 1 if grid[0][j] == 'C' else 0
    
    for i in range(n - 1):
        for j in range(3):
            if dp[i][j] != -1:
                for move in [-1, 0, 1]:
                    new_j = j + move
                    if 0 <= new_j < 3 and grid[i + 1][new_j] != 'W':
                        coins = 1 if grid[i + 1][new_j] == 'C' else 0
                        new_value = dp[i][j] + coins
                        if new_value > dp[i + 1][new_j]:
                            dp[i + 1][new_j] = new_value
    
    max_coins = 0
    for i in range(n):
        for j in range(3):
            if dp[i][j] > max_coins:
                max_coins = dp[i][j]
    
    print(max_coins)

if __name__ == "__main__":
    main()

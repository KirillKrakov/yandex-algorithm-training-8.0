def main():
    n, m = map(int, input().split())
    table = []
    for _ in range(n):
        row = list(map(int, input().split()))
        table.append(row)
    
    points = []
    for i in range(n):
        for j in range(m):
            points.append((table[i][j], i, j))
    
    points.sort()
    
    dp = [[1] * m for _ in range(n)]
    max_chain = 1
    
    for val, i, j in points:
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + dx, j + dy
            if 0 <= ni < n and 0 <= nj < m and table[ni][nj] == val - 1:
                dp[i][j] = max(dp[i][j], dp[ni][nj] + 1)
                max_chain = max(max_chain, dp[i][j])
    
    print(max_chain)

if __name__ == "__main__":
    main()

import sys

def main():
    s = input().strip()
    n = len(s)
    INF = 10**9
    dp = [[INF, INF] for _ in range(n+1)]
    dp[0][0] = 0

    for i, ch in enumerate(s, start=1):
        cost_left = 1 if ch in ('L', 'B') else 0
        cost_right = 1 if ch in ('R', 'B') else 0

        dp[i][0] = min(dp[i-1][0] + cost_left,
                       dp[i-1][1] + 1 + cost_left)

        dp[i][1] = min(dp[i-1][1] + cost_right,
                       dp[i-1][0] + 1 + cost_right)

    ans = min(dp[n][1], dp[n][0] + 1)
    print(ans)

if __name__ == '__main__':
    main()

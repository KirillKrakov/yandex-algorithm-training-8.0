import sys

def main():
    n = int(input())
    dp = [0] * (n + 1)
    dp[0] = 1

    for j in range(1, n + 1):
        for i in range(n, j - 1, -1):
            dp[i] += dp[i - j]

    print(dp[n])
    pass

if __name__ == '__main__':
    main()

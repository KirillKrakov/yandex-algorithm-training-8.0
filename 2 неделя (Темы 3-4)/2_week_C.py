import bisect

def main():
    n = int(input().strip())
    if n == 0:
        print(0.0)
        return
        
    intervals = []
    for _ in range(n):
        b, e, w = map(float, input().split())
        intervals.append((b, e, w))
        
    intervals.sort(key=lambda x: x[1])
    ends = [interval[1] for interval in intervals]
    dp = [0.0] * (n + 1)
    
    for i in range(1, n + 1):
        b, e, w = intervals[i-1]
        pos = bisect.bisect_right(ends, b) - 1
        prev_index = pos + 1
        dp[i] = max(dp[i-1], dp[prev_index] + w)
        
    print(f"{dp[n]:.6f}")

if __name__ == "__main__":
    main()

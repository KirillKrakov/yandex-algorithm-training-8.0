def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    value = [0] * (n - k + 1)
    for i in range(len(value)):
        s = sum(a[i:i+k])
        m = min(a[i:i+k])
        value[i] = s * m
        
    dp = [0] * (n + 1)
    prev = [-1] * (n + 1)
    
    for i in range(n):
        if dp[i] > dp[i + 1]:
            dp[i + 1] = dp[i]
            prev[i + 1] = i
            
        if i + k <= n and i < len(value):
            total = dp[i] + value[i]
            if total > dp[i + k]:
                dp[i + k] = total
                prev[i + k] = i
                
    towers = []
    current = n
    while current > 0:
        p = prev[current]
        if current - p == k:
            towers.append(p + 1)
        current = p
        
    towers.reverse()
    print(len(towers))
    if towers:
        print(' '.join(map(str, towers)))
        
if __name__ == "__main__":
    main()

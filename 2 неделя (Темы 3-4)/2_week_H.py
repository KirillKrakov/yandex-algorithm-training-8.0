def main():
    n = int(input().strip())
    
    if n == 0:
        print(2)
        return
        
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
                
    dp = [False] * (n + 1)
    
    dp[0] = False
    
    for i in range(1, n + 1):
        for take in [1, 2, 3]:
            if i - take >= 0:
                if not is_prime[i - take]:
                    if not dp[i - take]:
                        dp[i] = True
                        break
    
    print(1 if dp[n] else 2)

if __name__ == "__main__":
    main()

def main():
    n = int(input().strip())
    a = list(map(int, input().split()))
    diff = [0] * (n + 3)
    for j in range(1, n + 1):
        aj = a[j - 1]
        L = j + 1
        R = j + aj - 1
        if L <= R:
            if R > n:
                R = n
            diff[L] += 1
            diff[R + 1] -= 1
    cur = 0
    total = 0
    for i in range(1, n + 1):
        cur += diff[i]
        total += cur * a[i - 1]
    print(total)


if __name__ == "__main__":
    main()

def main():
    n, p = map(int, input().split())
    c_list = sorted(enumerate(list(map(int, input().split()))), key=lambda x: x[1])

    delta = 10**10
    ans = (0, 0)
    for i in range(1, n):
        idx1, ci = c_list[i]
        low = 0
        high = i - 1
        cur_delta = 10**10
        cur_i = idx1 + 1
        while low <= high:
            mid = (low + high) // 2
            idx2, cj = c_list[mid]
            if abs(ci / cj - p) < cur_delta:
                cur_delta = abs(ci / cj - p)
                cur_j = idx2 + 1
            if ci / cj > p:
                low = mid + 1
            else:
                high = mid - 1
        if cur_delta < delta:
            delta = cur_delta
            ans = (cur_i, cur_j)
    print(*ans)

if __name__ == '__main__':
    main()

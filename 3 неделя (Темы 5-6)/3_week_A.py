def main():
    a, b, S = map(int, input().split())
    low = max(a, b)
    high = max(a, b) + S + 1
    while low <= high:
        mid = (low + high) // 2
        cur_S = (mid - a) * (mid - b)
        if cur_S == S:
            print(mid)
            return
        elif cur_S < S:
            low = mid + 1
        else:
            high = mid - 1
    print(-1)


if __name__ == '__main__':
    main()

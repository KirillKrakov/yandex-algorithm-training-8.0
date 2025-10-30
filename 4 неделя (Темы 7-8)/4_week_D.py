import sys


def main():
    n = int(input())
    tables = list(map(int, input().split()))
    l, r = 0, n - 1
    sdv, sdm = tables[l], tables[r]
    final_diff, final_l, final_r = sum(tables) * 2, -1, -1
    while l < r:
        cur_diff = sdv - sdm
        if abs(cur_diff) < final_diff:
            final_diff = abs(cur_diff)
            final_l = l + 1
            final_r = r + 1
        if cur_diff == 0:
            print(0, l + 1, r + 1)
            return
        elif cur_diff < 0:
            l += 1
            sdv += tables[l]
        else:
            r -= 1
            sdm += tables[r]
    print(final_diff, final_l, final_r)
    pass


if __name__ == '__main__':
    main()

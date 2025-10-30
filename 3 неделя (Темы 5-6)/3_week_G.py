from bisect import bisect_right

def sum_abs_with_sorted(x, sorted_arr, pref):
    L = len(sorted_arr)
    k = bisect_right(sorted_arr, x)
    sum_le = pref[k]
    sum_gt = pref[L] - sum_le
    return x * k - sum_le + sum_gt - x * (L - k)

def main():
    n = int(input().strip())
    a = list(map(int, input().split()))
    m = int(input().strip())
    b = list(map(int, input().split()))

    sb = sorted(b)
    pref_b = [0] * (m + 1)
    for i in range(m):
        pref_b[i+1] = pref_b[i] + sb[i]

    sa = sorted(a)
    pref_a = [0] * (n + 1)
    for i in range(n):
        pref_a[i+1] = pref_a[i] + sa[i]

    partA = 0
    for idx, val in enumerate(a, start=1):
        s = sum_abs_with_sorted(val, sb, pref_b)
        partA += idx * s

    partB = 0
    for idx, val in enumerate(b, start=1):
        s = sum_abs_with_sorted(val, sa, pref_a)
        partB += idx * s

    result = partA - partB
    print(result)

if __name__ == "__main__":
    main()
import sys

def main():
    n = int(input())
    a = list(map(int, input().split()))
    vasya = a[0: n: 2]
    masha = a[1: n: 2]
    x1 = min(vasya)
    x2 = max(masha)
    if x2 > x1:
        delta = x2 - x1
        print((sum(vasya) + delta) - (sum(masha) - delta))
    else:
        print(sum(vasya) - sum(masha))
    pass


if __name__ == '__main__':
    main()

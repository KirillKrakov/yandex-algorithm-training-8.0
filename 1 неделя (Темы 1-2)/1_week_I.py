import sys

def min_maneuvers(x, y, f, g):
    dx = abs(f - x)
    dy = abs(g - y)
    a = max(dx, dy)
    b = min(dx, dy)

    if a == 0 and b == 0:
        n = 0
    elif b == 0:
        n = 3 * a - 2
    elif b == 1:
        n = 3 * a - 1
    else:
        n = 3 * (a + b) - 4

    return 0 if n == 0 else n - 1

def main():
    x, y = map(int, input().split())
    f, g = map(int, input().split())
    print(min_maneuvers(x, y, f, g))
    pass


if __name__ == '__main__':
    main()

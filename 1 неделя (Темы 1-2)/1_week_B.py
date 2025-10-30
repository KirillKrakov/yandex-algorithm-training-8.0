import sys


def main():
    a, b, c, v0, v1, v2 = map(int, input().split())
    x1 = min(a, b + c)
    x2 = min(b, a + c)
    x3 = min(c, a + b)
    times = [0] * 4
    # 1 путь: дом, супермаркет, пункт выдачи, дом
    times[0] = round(x1 / v0 + x3 / v1 + x2 / v2, 4)
    # 2 путь: дом, супермаркет, дом, пункт выдачи, дом
    times[1] = round(x1 / v0 + x1 / v1 + x2 / v0 + x2 / v1, 4)
    # 3 путь: дом, пункт выдачи, супермаркет, дом
    times[2] = round(x2 / v0 + x3 / v1 + x1 / v2, 4)
    # 4 путь: дом, пункт выдачи, дом, супермаркет, дом
    times[3] = round(x2 / v0 + x2 / v1 + x1 / v0 + x1 / v1, 4)
    print(min(times))
    pass


if __name__ == '__main__':
    main()

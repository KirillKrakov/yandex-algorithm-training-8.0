import sys


def main():
    n, k = map(int, input().split())

    if k == 0:
        print(n)
        return

    # выходим на цикл (%10 in [2, 4, 6, 8]) или останавливаемся (% 10 == 0)
    while k > 0 and n % 10 != 0:
        if n % 10 == 5:
            n += 5
            k -= 1
            break
        if n % 10 in (2, 4, 8, 6):
            break
        n += n % 10
        k -= 1

    # обработка цикла
    if k > 0 and n % 10 != 0:
        cycles = k // 4
        rem = k % 4
        n += cycles * 20
        for _ in range(rem):
            n += n % 10

    print(n)
    pass


if __name__ == '__main__':
    main()

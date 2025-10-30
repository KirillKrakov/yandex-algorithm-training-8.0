import sys


def main():
    n = int(input())
    array = [[0,0,0] for _ in range(n)]
    for i in range(n):
        if i < 3:
            array[i][i] = 1
        if i > 0:
            array[i][0] = sum(array[i-1])
        if i > 1:
            array[i][1] = sum(array[i-2])
        if i > 2:
            array[i][2] = sum(array[i-3])
    print(sum(array[n-1]))
    pass


if __name__ == '__main__':
    main()

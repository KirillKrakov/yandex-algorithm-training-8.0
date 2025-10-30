import sys


def main():
    scanline = []

    n = int(input())
    for _ in range(n):
        power, bid = map(int, input().split())
        scanline.append((power, bid, -1))
    
    m = int(input())
    for i in range(m):
        power = int(input())
        scanline.append((power, 0,  i))

    scanline.sort()
    current_bid = 0
    answer = [0] * m
    for power, bid, idx in scanline:
        if bid != 0:
            current_bid = bid
        else:
            answer[idx] = power * current_bid
    for elem in answer:
        print(elem)
    pass


if __name__ == '__main__':
    main()

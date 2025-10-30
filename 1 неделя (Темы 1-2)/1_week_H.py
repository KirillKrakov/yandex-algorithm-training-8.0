import sys


def main():
    n, m = map(int, input().split())
    s = input()
    s_parts = {}
    result = [0] * m
    for i in range(m):
        cur_part = s[(n//m)*i:(n//m)*(i+1)]
        s_parts.setdefault(cur_part, set()).add(i)
    for i in range(m):
        t = input()
        result[s_parts[t].pop()] = i + 1
    print(*result)
    pass


if __name__ == '__main__':
    main()

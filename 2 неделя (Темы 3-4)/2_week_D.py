import sys

def main():
    data = sys.stdin.read().splitlines()

    s = data[0].strip()
    ptr = 1
    n = int(data[ptr].strip()) if ptr < len(data) else 0
    ptr += 1

    words = []
    for i in range(n):
        if ptr + i < len(data):
            words.append(data[ptr + i].strip())
        else:
            words.append('')

    # сгруппируем слова по длине в множества для O(1)-проверки принадлежности
    bylen = {}
    maxL = 0
    for w in words:
        l = len(w)
        maxL = max(maxL, l)
        bylen.setdefault(l, set()).add(w)

    L = len(s)
    reachable = [False] * (L + 1)
    parent = [None] * (L + 1)
    reachable[0] = True

    for i in range(L):
        if not reachable[i]:
            continue
        # пробуем все возможные длины слова от позиции i
        limit = min(maxL, L - i)
        for l in range(1, limit + 1):
            sub = s[i:i + l]
            if sub in bylen.get(l, ()):
                j = i + l
                if not reachable[j]:
                    reachable[j] = True
                    parent[j] = (i, sub)
        if reachable[L]:
            break

    # восстанавливаем разбиение (гарантируется что решение есть)
    res = []
    pos = L
    while pos > 0:
        prev = parent[pos]
        i, w = prev
        res.append(w)
        pos = i

    res.reverse()
    print(" ".join(res))
    pass


if __name__ == '__main__':
    main()

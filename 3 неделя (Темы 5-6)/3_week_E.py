def main():
    n = int(input())
    graph = {i: [] for i in range(n)}

    # читаем родителей и строим дерево
    for i in range(1, n):
        p = int(input())
        graph.setdefault(p, []).append(i)

    # балансы городов
    a = list(map(int, input().split()))

    # считаем количество эдиктов
    ans = 0
    for v in range(n):
        sum_children = sum(a[c] for c in graph.get(v, []))
        op_v = -a[v] + sum_children
        ans += abs(op_v)

    print(ans)


if __name__ == '__main__':
    main()

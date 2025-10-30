def main():
    n = int(input())
    a_vals = list(map(int, input().split()))
    a = [0] * (n + 1)
    for i in range(1, n + 1):
        a[i] = a_vals[i-1]

    g = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)

    parent = [0] * (n + 1)
    order = []
    stack = [1]
    parent[1] = -1
    while stack:
        v = stack.pop()
        order.append(v)
        for to in g[v]:
            if to == parent[v]:
                continue
            parent[to] = v
            stack.append(to)

    subtree = a[:]
    for v in reversed(order):
        for to in g[v]:
            if to == parent[v]:
                continue
            subtree[v] += subtree[to]

    total = subtree[1]
    best_node = 1
    best_val = 10**30

    for v in range(1, n + 1):
        max_queue = a[v]
        for to in g[v]:
            if to == parent[v]:
                comp = total - subtree[v]
            else:
                comp = subtree[to]
            if comp > max_queue:
                max_queue = comp
        if max_queue < best_val:
            best_val = max_queue
            best_node = v

    print(best_node)

if __name__ == "__main__":
    main()

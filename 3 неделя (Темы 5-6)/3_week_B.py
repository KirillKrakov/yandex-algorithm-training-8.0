from collections import deque

def main():
    n = int(input())
    graph = {}
    tupics = set()
    for _ in range(n-1):
        a, b = map(int, input().split())
        graph.setdefault(a, set()).add(b)
        graph.setdefault(b, set()).add(a)
    
    for node, neighbors in graph.items():
        if len(neighbors) == 1:
            tupics.add(node)

    queue = deque()
    dist = {}
    src = {}

    for t in tupics:
        queue.append(t)
        dist[t] = 0
        src[t] = t

    min_len = 10**9
    while queue:
        v = queue.popleft()
        for u in graph.get(v, []):
            if u not in dist:
                dist[u] = dist[v] + 1
                src[u] = src[v]
                queue.append(u)
            elif src[u] != src[v]:
                min_len = min(min_len, dist[u] + dist[v] + 1)
    print(min_len)


if __name__ == '__main__':
    main()

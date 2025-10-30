from collections import defaultdict

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    children = defaultdict(list)
    roots = []
    for i in range(n):
        v = i+1
        p = arr[i]
        if p == 0:
            roots.append(v)
        else:
            children[p].append(v)

    tin = [0] * (n + 1)
    tout = [0] * (n + 1)
    timer = 0
    stack = []
    for r in roots:
        stack.append((r, 0)) 
        while stack:
            v, st = stack.pop()
            if st == 0:
                timer += 1
                tin[v] = timer
                stack.append((v, 1))
                for c in reversed(children[v]):
                    stack.append((c, 0))
            else:
                tout[v] = timer

    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        print(1 if tin[a] < tin[b] <= tout[a] else 0)

if __name__ == '__main__':
    main()

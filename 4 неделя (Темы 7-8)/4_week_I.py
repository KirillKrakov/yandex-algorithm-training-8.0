import math

def build_offsets(d):
    offsets = set()
    lim = math.isqrt(d)
    for dx in range(lim + 1):
        dy2 = d - dx*dx
        if dy2 < 0:
            continue
        dy = math.isqrt(dy2)
        if dy*dy != dy2:
            continue
        for sx in (1, -1):
            for sy in (1, -1):
                offsets.add((sx * dx, sy * dy))
                offsets.add((sx * dy, sy * dx))
    offsets.discard((0, 0))
    return list(offsets)

def main():
    n, d = map(int, input().split())
    points = []
    pts_set = set()
    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
        pts_set.add((x, y))

    offsets = build_offsets(d)

    ans = 0
    for x, y in points:
        for ox, oy in offsets:
            nx, ny = x + ox, y + oy
            if (nx, ny) in pts_set:
                if (x, y) < (nx, ny):
                    ans += 1

    print(ans)

if __name__ == "__main__":
    main()

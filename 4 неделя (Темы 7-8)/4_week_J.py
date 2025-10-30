import sys
from math import gcd
from functools import cmp_to_key

input = sys.stdin.readline

def time_cmp(a, b):
    an, ad = a; bn, bd = b
    left = an * bd
    right = bn * ad
    if left < right:
        return -1
    if left > right:
        return 1
    return 0

def add_event(events_dict, num, den, ev):
    if den == 0:
        return
    if num * den <= 0:
        return
    g = gcd(abs(num), abs(den))
    num //= g
    den //= g
    if den < 0:
        num = -num
        den = -den
    key = (num, den)
    if key in events_dict:
        events_dict[key].append(ev)
    else:
        events_dict[key] = [ev]

def main():
    data = input().split()
    if not data:
        return
    N = int(data[0]); L = int(data[1]); W = int(data[2])
    xs = [0]*N; ys = [0]*N; vxs = [0]*N; vys = [0]*N
    for i in range(N):
        x,y,vx,vy = map(int, input().split())
        xs[i]=x; ys[i]=y; vxs[i]=vx; vys[i]=vy

    events = {}

    for i in range(N):
        xi, yi, vxi, vyi = xs[i], ys[i], vxs[i], vys[i]
        if vxi != 0:
            add_event(events, L - xi, vxi, ('finish', i))
        if vyi != 0:
            add_event(events, -yi, vyi, ('wall', i))
            add_event(events, W - yi, vyi, ('wall', i))

    for i in range(N):
        xi, yi, vxi, vyi = xs[i], ys[i], vxs[i], vys[i]
        for j in range(i+1, N):
            xj, yj, vxj, vyj = xs[j], ys[j], vxs[j], vys[j]
            dx = xj - xi
            dy = yj - yi
            dvx = vxi - vxj
            dvy = vyi - vyj

            if dvx == 0 and dvy == 0:
                continue
            if dvx == 0:
                if dx != 0:
                    continue
                if dvy == 0:
                    continue
                add_event(events, dy, dvy, ('col', i, j))
            elif dvy == 0:
                if dy != 0:
                    continue
                add_event(events, dx, dvx, ('col', i, j))
            else:
                if dx * dvy != dy * dvx:
                    continue
                if dx * dvx <= 0:
                    continue
                add_event(events, dx, dvx, ('col', i, j))

    if not events:
        print(0)
        print()
        return

    times = sorted(events.keys(), key=cmp_to_key(time_cmp))

    active = [True]*N

    for num, den in times:
        group = events[(num, den)]
        involved = set()
        for ev in group:
            if ev[0] == 'finish' or ev[0] == 'wall':
                involved.add(ev[1])
            else:
                involved.add(ev[1]); involved.add(ev[2])

        involved_active = [i for i in involved if active[i]]
        if not involved_active:
            continue

        pos_map = {}
        wall_hit = set()
        for i in involved_active:
            xnum = xs[i] * den + vxs[i] * num
            ynum = ys[i] * den + vys[i] * num
            key = (xnum, ynum)
            if key in pos_map:
                pos_map[key].append(i)
            else:
                pos_map[key] = [i]
            if ynum == 0 or ynum == W * den:
                wall_hit.add(i)

        collision = set()
        for lst in pos_map.values():
            if len(lst) >= 2:
                collision.update(lst)

        to_elim = collision.union(wall_hit)
        for idx in to_elim:
            active[idx] = False

        finishers = []
        for key, lst in pos_map.items():
            xnum, ynum = key
            if xnum == L * den:
                if len(lst) >= 2:
                    for idx in lst:
                        active[idx] = False
                    continue
                idx = lst[0]
                if not active[idx]:
                    continue
                finishers.append(idx)

        if finishers:
            finishers.sort()
            print(len(finishers))
            print(" ".join(str(i+1) for i in finishers))
            return

    print(0)
    print()

if __name__ == "__main__":
    main()

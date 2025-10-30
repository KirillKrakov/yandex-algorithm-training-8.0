import sys

def main():
    n, m, x = map(int, input().split())
    events = []
    for _ in range(n):
        a, b, v = map(int, input().split())
        if a < b:
            if a > x:
                continue
            if b < x:
                t_start = (x - b) / v
            else:
                t_start = 0.0
            t_end = (x - a) / v
        else:
            if a < x:
                continue
            if b > x:
                t_start = (b - x) / v
            else:
                t_start = 0.0
            t_end = (a - x) / v

        events.append((t_start, 0, -1))
        events.append((t_end, 2, -1))

    car_times = list(map(int, input().split()))
    for idx, t in enumerate(car_times):
        events.append((float(t), 1, idx))

    events.sort()

    train_count = 0
    pending = []
    ans = [0.0] * m

    for time, typ, idx in events:
        if typ == 0:
            train_count += 1
        elif typ == 2:
            train_count -= 1
            if train_count == 0 and pending:
                for car_idx in pending:
                    ans[car_idx] = time
                pending.clear()
        else:
            if train_count == 0:
                ans[idx] = time
            else:
                pending.append(idx)

    if pending:
        last_time = events[-1][0]
        for car_idx in pending:
            ans[car_idx] = last_time

    out = sys.stdout
    for v in ans:
        out.write("{:.7f}\n".format(v))

if __name__ == '__main__':
    main()

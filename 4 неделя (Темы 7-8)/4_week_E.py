def main():
    n, m, k = map(int, input().split())
    potholes = list(map(int, input().split()))

    diff = [0] * (n + 1)
    for _ in range(m):
        l, r = map(int, input().split())
        diff[l - 1] += 1
        if r < n:
            diff[r] -= 1

    bus_counts = [0] * n
    cur = 0
    for i in range(n):
        cur += diff[i]
        bus_counts[i] = cur

    pairs = list(enumerate(bus_counts))
    bc_pairs = [(bc, idx) for idx, bc in pairs]
    bc_pairs.sort(reverse=True)
    answer = 0
    for bus_count, road_id in bc_pairs:
        if bus_count == 0:
            break

        if k <= 0:
            answer += bus_count * potholes[road_id]
            continue

        if potholes[road_id] <= k:
            k -= potholes[road_id]
            remaining = 0
        else:
            remaining = potholes[road_id] - k
            k = 0

        answer += bus_count * remaining
    print(answer)

if __name__ == '__main__':
    main()

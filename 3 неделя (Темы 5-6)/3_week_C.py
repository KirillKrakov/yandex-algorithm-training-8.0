def main():
    N, W, H = map(float, input().split())
    N = int(N)
    words = {}
    for i in range(N):
        words[i] = tuple(map(float, input().split()))

    def check(k):
        eps = 1e-12
        total_height = 0.0
        cur_width = 0.0
        cur_height = 0.0

        for i in range(N):
            a, b = words[i]
            w = a * k
            h = b * k

            if w > W + eps:
                return False

            if cur_width <= eps:
                cur_width = w
                cur_height = h
                continue

            if abs(h - cur_height) <= 1e-9:
                if cur_width + w <= W + eps:
                    cur_width += w
                else:
                    total_height += cur_height
                    if total_height > H + eps:
                        return False
                    cur_width = w
                    cur_height = h
            else:
                total_height += cur_height
                if total_height > H + eps:
                    return False
                cur_width = w
                cur_height = h

        total_height += cur_height
        return total_height <= H + eps

    high = min((W / a) for a, b in words.values())
    low = 0.0

    for _ in range(60):
        mid = (low + high) / 2
        if check(mid):
            low = mid
        else:
            high = mid

    print(f"{low:.6f}")


if __name__ == '__main__':
    main()

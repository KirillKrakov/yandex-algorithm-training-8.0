from collections import deque

def main():
    n, L = map(int, input().split())
    P, R, Q, F = [], [], [], []
    totalF = 0
    for _ in range(n):
        Pi, Ri, Qi, Fi = map(int, input().split())
        P.append(Pi)
        R.append(Ri)
        Q.append(Qi)
        F.append(Fi)
        totalF += Fi

    if totalF < L:
        print(-1)
        return

    INF = 10**18
    dp = [INF] * (totalF + 1)
    dp[0] = 0
    parent = [[-1] * (totalF + 1) for _ in range(n + 1)]
    choice = [[0] * (totalF + 1) for _ in range(n + 1)]

    cur_sum = 0
    for i in range(1, n + 1):
        Fi, Pi, Ri, Qi = F[i - 1], P[i - 1], R[i - 1], Q[i - 1]
        newdp = [INF] * (totalF + 1)
        fvals = [dp[t] - t * Pi for t in range(cur_sum + 1)]
        dq = deque()
        maxk = cur_sum + Fi
        for k in range(maxk + 1):
            left = k - Fi
            if k <= cur_sum:
                while dq and fvals[dq[-1]] > fvals[k]:
                    dq.pop()
                dq.append(k)
            while dq and dq[0] < left:
                dq.popleft()
            if dq:
                t0 = dq[0]
                cand = k * Pi + fvals[t0]
                x = k - t0
                if cand < newdp[k] or (cand == newdp[k] and x > choice[i][k]):
                    newdp[k], parent[i][k], choice[i][k] = cand, t0, x

        gvals = [dp[t] - t * Qi for t in range(cur_sum + 1)]
        dq.clear()
        for k in range(maxk + 1):
            right2 = k - Ri
            if 0 <= right2 <= cur_sum:
                while dq and gvals[dq[-1]] > gvals[right2]:
                    dq.pop()
                dq.append(right2)
            left2 = k - Fi
            while dq and dq[0] < left2:
                dq.popleft()
            if dq:
                t0 = dq[0]
                x = k - t0
                if x >= Ri:
                    cand = k * Qi + gvals[t0]
                    if cand < newdp[k] or (cand == newdp[k] and x > choice[i][k]):
                        newdp[k], parent[i][k], choice[i][k] = cand, t0, x

        dp = newdp
        cur_sum += Fi

    best_cost = INF
    best_s = -1
    for s in range(L, totalF + 1):
        if dp[s] < best_cost:
            best_cost, best_s = dp[s], s

    if best_cost == INF:
        print(-1)
        return

    ans = [0] * n
    s = best_s
    for i in range(n, 0, -1):
        x = choice[i][s]
        ans[i - 1] = x
        s = parent[i][s]
        if s == -1:
            s = 0

    print(best_cost)
    print(*ans)

if __name__ == "__main__":
    main()

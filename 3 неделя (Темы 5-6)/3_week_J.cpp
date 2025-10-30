#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    if (!(cin >> n)) return 0;
    vector<ll> a(n), b(n);
    ll suma = 0, sumb = 0;
    for (int i = 0; i < n; ++i) { cin >> a[i]; suma += a[i]; }
    for (int i = 0; i < n; ++i) { cin >> b[i]; sumb += b[i]; }

    if (suma > sumb) { cout << -1 << '\n'; return 0; }

    vector<int> q(n);

    auto can = [&](int k) -> bool {
        int head = 0, tail = 0;
        int p = 0;
        ll rem = 0;

        for (int j = 0; j < n; ++j) {
            int add_up_to = j + k;
            if (add_up_to > n - 1) add_up_to = n - 1;
            while (p <= add_up_to) {
                q[tail++] = p;
                ++p;
            }

            ll cap = b[j];
            while (head < tail && cap > 0) {
                int idx = q[head];
                if ((ll)idx + k < j) return false;
                if (rem == 0) rem = a[idx];
                if (rem <= cap) {
                    cap -= rem;
                    rem = 0;
                    ++head;
                } else {
                    rem -= cap;
                    cap = 0;
                    break;
                }
            }
            if (head < tail) {
                int idx = q[head];
                if ((ll)idx + k < j) return false;
            }
        }
        return (head == tail) && rem == 0;
    };

    int low = 0, high = n, ans = -1;
    while (low <= high) {
        int mid = (low + high) >> 1;
        if (can(mid)) { ans = mid; high = mid - 1; }
        else low = mid + 1;
    }

    cout << ans << '\n';
    return 0;
}

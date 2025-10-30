import sys


def main():
    events = []

    n = int(input())
    for _ in range(n):
        n_str, m_str = input().split("-")
        n_hh,n_mm = map(int, n_str.split(":"))
        m_hh,m_mm = map(int, m_str.split(":"))
        n_time = n_hh * 60 + n_mm
        m_time = m_hh * 60 + m_mm
        # 2 - уехал, 1 - приехал
        events.append((n_time, "N", 2))
        events.append((m_time, "M", 1))

    m = int(input())
    for _ in range(m):
        n_str, m_str = input().split("-")
        n_hh,n_mm = map(int, n_str.split(":"))
        m_hh,m_mm = map(int, m_str.split(":"))
        n_time = n_hh * 60 + n_mm
        m_time = m_hh * 60 + m_mm
        events.append((n_time, "M", 2))
        events.append((m_time, "N", 1))
    
    events.sort()
    answer, cur_in_n, cur_in_m = 0, 0, 0
    for _time, office, delta in events:
        if office == "N":
            if delta == 2:
                if cur_in_n == 0:
                    answer += 1
                    cur_in_n += 1
                cur_in_n -= 1
            else:
                cur_in_n += 1
        if office == "M":
            if delta == 2:
                if cur_in_m == 0:
                    answer += 1
                    cur_in_m += 1
                cur_in_m -= 1
            else:
                cur_in_m += 1
    print(answer)
    pass


if __name__ == '__main__':
    main()

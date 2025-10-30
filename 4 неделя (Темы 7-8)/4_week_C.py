from collections import deque

def main():
    _n, x = map(int, input().split())
    queue = deque()
    queue.append(0)
    queue_ptr = 0
    for elem in list(map(int, input().split())):
        queue.append(queue[-1] + int(elem >= x))
    m = int(input())
    for _ in range(m):
        act_str = input()
        if act_str == "2":
            queue_ptr += 1
        elif act_str.startswith("1"):
            cur_a = int((act_str.split())[1])
            queue.append(queue[-1] + int(cur_a >= x))
        elif act_str.startswith("3"):
            k = int((act_str.split())[1]) + queue_ptr
            print(queue[k] - queue[queue_ptr])
    pass


if __name__ == '__main__':
    main()

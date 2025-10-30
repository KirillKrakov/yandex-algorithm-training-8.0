import sys

input = sys.stdin.readline

class ListObj:
    __slots__ = ('root','start','length','is_root')
    def __init__(self, root, start, length, is_root):
        self.root = root    # python list reference
        self.start = start  # 0-based index in root
        self.length = length
        self.is_root = is_root

    def get(self, i):
        return self.root[self.start + i - 1]

    def set(self, i, x):
        self.root[self.start + i - 1] = x

    def add(self, x):
        # only allowed if originally created by "new List(...)"
        if self.is_root:
            self.root.append(x)
            self.length += 1

def parse_numbers_inside(s):
    # s contains stuff like "new List(1,2,3)" or "(1,2)" -> we want substring inside parentheses
    l = s.find('(')
    r = s.rfind(')')
    if l == -1 or r == -1 or r <= l+1:
        return []
    subs = s[l+1:r]
    if subs == '':
        return []
    return list(map(int, subs.split(',')))

def main():
    n_line = input().strip()
    if not n_line:
        return
    n = int(n_line)
    vars = {}  # name -> ListObj
    out_lines = []

    for _ in range(n):
        line = input().strip()
        if not line:
            continue

        # Creation forms start with "List "
        if line.startswith("List "):
            eq = line.find('=')
            left = line[5:eq].strip()  # between "List " and '='
            right = line[eq+1:].strip()
            if right.startswith("new List"):
                nums = parse_numbers_inside(right)
                root = list(nums)
                obj = ListObj(root, 0, len(root), True)
                vars[left] = obj
            else:
                # form "a.subList(from,to)"
                # right likely like "a.subList(2,3)"
                dot = right.find('.')
                src_name = right[:dot]
                # parse numbers
                nums = parse_numbers_inside(right)
                if len(nums) >= 2:
                    fr, to = nums[0], nums[1]
                else:
                    fr = to = 0
                parent = vars[src_name]
                start = parent.start + (fr - 1)
                length = to - fr + 1
                obj = ListObj(parent.root, start, length, False)
                vars[left] = obj
        else:
            # operations: "a.set(i,x)" or "a.add(x)" or "a.get(i)"
            dot = line.find('.')
            name = line[:dot]
            op = line[dot+1:]
            if op.startswith("set"):
                # set(i,x)
                nums = parse_numbers_inside(op)
                i = nums[0]; x = nums[1]
                vars[name].set(i, x)
            elif op.startswith("add"):
                nums = parse_numbers_inside(op)
                x = nums[0]
                vars[name].add(x)
            elif op.startswith("get"):
                nums = parse_numbers_inside(op)
                i = nums[0]
                val = vars[name].get(i)
                out_lines.append(str(val))
            else:
                # unknown op - shouldn't happen
                pass

    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()

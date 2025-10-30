import sys
from collections import Counter

def main():
    s = input().strip()
    n = len(s)

    freq = {}
    for char in s:
        if char not in freq:
            freq[char] = 0
        freq[char] += 1
        
    total_pairs = n * (n - 1) // 2
    same_pairs = 0
    for count in freq.values():
        same_pairs += count * (count - 1) // 2
        
    result = 1 + (total_pairs - same_pairs)
    print(result)
    pass


if __name__ == '__main__':
    main()

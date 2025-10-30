import sys


def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    freq = {}
    for c in a:
        if c not in freq:
            freq[c] = 0
        freq[c] += 1
    topics = sorted(freq.keys(), key=lambda x: freq[x], reverse=True)
    unique_topics = min(len(topics), k)
    result = []
    for i in range(unique_topics):
        result.append(topics[i])
    remaining = k - unique_topics
    if remaining > 0:
        idx = 0
        while remaining > 0:
            topic = topics[idx]
            available = freq[topic] - 1
            if available > 0:
                result.append(topic)
                remaining -= 1
            idx = (idx + 1) % len(topics)
    
    print(' '.join(map(str, result)))

if __name__ == '__main__':
    main()

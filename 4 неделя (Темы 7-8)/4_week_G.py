def main():
    n = int(input().strip())
    series_counts = list(map(int, input().split()))
    importance = list(map(int, input().split()))

    seasons = list(zip(series_counts, importance))
    seasons.sort()

    total_importance = sum(importance)
    half_weight = (total_importance + 1) // 2

    cumulative_weight = 0
    optimal_episodes = None
    for episodes, weight in seasons:
        cumulative_weight += weight
        if cumulative_weight >= half_weight:
            optimal_episodes = episodes
            break

    total_penalty = 0
    for episodes, weight in seasons:
        total_penalty += weight * abs(optimal_episodes - episodes)

    print(optimal_episodes, total_penalty)


if __name__ == '__main__':
    main()

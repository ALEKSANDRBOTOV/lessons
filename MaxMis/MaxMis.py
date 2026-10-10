def max_gap(times):
    if len(times)<2:
        return 0
    return max(times[i + 1] - times[i] for i in range(len(times) - 1))# Находим максимальную разницу между пингами

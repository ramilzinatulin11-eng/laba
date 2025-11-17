def time_series_analysis(series, p):
    # Математическое ожидание
    mean = sum(series) / len(series)
    
    # Дисперсия
    variance = sum((x - mean) ** 2 for x in series) / len(series)
    
    # СКО
    std = variance ** 0.5
    
    # Локальные максимумы и минимумы
    local_max = []
    local_min = []
    
    for i in range(1, len(series) - 1):
        if series[i] > series[i-1] and series[i] > series[i+1]:
            local_max.append((i, series[i]))
        elif series[i] < series[i-1] and series[i] < series[i+1]:
            local_min.append((i, series[i]))
    
    # Скользящее среднее
    moving_avg = []
    for i in range(len(series) - p + 1):
        window = series[i:i + p]
        avg = sum(window) / p
        moving_avg.append(avg)
    
    return {
        'mean': mean,
        'variance': variance,
        'std': std,
        'local_maxima': local_max,
        'local_minima': local_min,
        'moving_average': moving_avg
    }

# Тесты
series1 = [1, 3, 2, 5, 4, 6, 3, 2, 4, 7]
series2 = [2, 4, 1, 5, 3, 6, 2, 7, 1]

print("Тест 1:")
result1 = time_series_analysis(series1, 3)
print(f"Мат.ожидание: {result1['mean']:.2f}")
print(f"Дисперсия: {result1['variance']:.2f}")
print(f"СКО: {result1['std']:.2f}")
print(f"Локальные максимумы: {result1['local_maxima']}")
print(f"Локальные минимумы: {result1['local_minima']}")
print(f"Скользящее среднее (p=3): {[round(x, 2) for x in result1['moving_average']]}")

print("\nТест 2:")
result2 = time_series_analysis(series2, 2)
print(f"Мат.ожидание: {result2['mean']:.2f}")
print(f"Дисперсия: {result2['variance']:.2f}")
print(f"СКО: {result2['std']:.2f}")
print(f"Локальные максимумы: {result2['local_maxima']}")
print(f"Локальные минимумы: {result2['local_minima']}")
print(f"Скользящее среднее (p=2): {[round(x, 2) for x in result2['moving_average']]}")
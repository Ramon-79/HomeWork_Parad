import math


def pearson_correlation(array_1, array_2):

    if len(array_1) != len(array_2):
        raise ValueError("Массивы должны быть одинаковой длины")

    n = len(array_1)

    mean_x = sum(array_1) / n
    mean_y = sum(array_2) / n

    variance_x = sum([(xi - mean_x) ** 2 for xi in array_1]) / float(len(array_1))
    variance_y = sum([(yi - mean_y) ** 2 for yi in array_2]) / float(len(array_2))

    covariance = sum([(xi - mean_x) * (yi - mean_y) for xi, yi in zip(array_1, array_2)]) / float(len(array_1))
    correlation = covariance / (math.sqrt(variance_x * variance_y))

    return correlation


array_1 = [13, 21, 32, 4, 56, 7, 877]
array_2 = [67, 76, 89, 98, 52, 6, 77]

correlation = round(pearson_correlation(array_1, array_2), 4)
print(f"Корреляция Пирсона: {correlation}")

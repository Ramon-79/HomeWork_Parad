from typing import List


def binary_search(arr: List[int], number: int) -> int:
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == number:
            return mid
        elif arr[mid] < number:
            left = mid + 1
        else:
            right = mid - 1

    return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(f"Исходный массив: {arr}")
number = int(input("Введите число: "))
result = binary_search(arr, number)

if result == -1:
    print("Искомого числа нет в массиве")
else:
    print(f"Искомое число: {number} найдено по индексу: {result}")

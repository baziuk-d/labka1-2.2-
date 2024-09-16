def array_monotonic(arr):
    if arr[0] > arr[len(arr) - 1]:  # тут перевірка чи масив спадає
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:  # тут перевірка чи елементи зростають
                return False
    else:
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:  # перевірка чи елементи спадають
                return False
    return True
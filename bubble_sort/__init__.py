def bubble_sort(original_list = []):
    arr = original_list.copy()
    list_len = len(arr)
    count = 0

    for i in range(list_len):
        swapped = False
        count += 1
        for j in range (list_len - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    print()
    print(f'Counter: {count}')
    print()

    return arr

def bubble_sort(original_list = []):
    copy_list = original_list.copy()
    while True:
        swapped = False
        for i in range(len(copy_list)):
            if copy_list[i] > copy_list[i+1]:
                pivot = copy_list[i]
                copy_list[i] = copy_list[i+1]
                copy_list[i+1] = pivot
                swapped = True

            if i == len(copy_list) - 2:
                break

        if not swapped:
            break

    return copy_list

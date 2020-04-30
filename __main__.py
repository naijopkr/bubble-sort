from bubble_sort import bubble_sort
from random import randint

if __name__ == '__main__':
    unsorted_list = []
    for i in range(10):
        unsorted_list.append(randint(0, 100))

    sorted_list = bubble_sort(unsorted_list)

    print('### ORIGINAL ###')
    print(unsorted_list)
    print()
    print('### SORTED ###')
    print(sorted_list)

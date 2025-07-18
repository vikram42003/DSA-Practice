def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def test_insertion_sort():
    test_cases = [
        ([], []),  # empty array
        ([1], [1]),  # single element
        ([2, 1], [1, 2]),  # two elements, reversed
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),  # already sorted
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),  # reversed array
        ([3, 1, 2, 1, 3], [1, 1, 2, 3, 3]),  # duplicates
        ([9, -3, 5, 0, -2, 1], [-3, -2, 0, 1, 5, 9]),  # mixed positive and negative
    ]

    for i, (input_arr, expected) in enumerate(test_cases):
        arr_copy = input_arr.copy()
        insertion_sort(arr_copy)
        assert (
            arr_copy == expected
        ), f"Test case {i+1} failed: got {arr_copy}, expected {expected}"
        print(f"Test case {i+1} passed.")


test_insertion_sort()

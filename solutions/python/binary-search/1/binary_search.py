def find(search_list, value):
    """Find the index of a value in a sorted list using binary search.
    
    Raises:
        ValueError: If the value is not present in the array.
    """
    left = 0
    right = len(search_list) - 1

    while left <= right:
        middle = (left + right) // 2
        middle_element = search_list[middle]

        if middle_element == value:
            return middle
        elif middle_element < value:
            left = middle + 1
        else:
            right = middle - 1

    raise ValueError("value not in array")
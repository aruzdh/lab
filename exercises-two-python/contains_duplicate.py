def contains_duplicate(nums, k: int) -> bool:
    """
    Checks if there are any duplicate values in the list within k distance of each other.

    Args:
        nums: A list of integers to check for duplicates
        k (int): The maximum distance between duplicate values to consider

    Returns:
        bool: True if there are duplicates within k distance, False otherwise
    """
    numbers = {}
    for index, num in enumerate(nums):
        if num not in numbers:
            numbers[num] = [index]
        else:
            indexes = numbers[num]
            for i in indexes:
                if abs(index - i) <= k:
                    return True
            indexes.append(index)
            numbers[num] = indexes
    return False

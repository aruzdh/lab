# Time complexity is O(n), where n is the number of elements in the list, with O(n) space for the set of repeated elements.
def single_number(nums):
    """
    Finds the element that appears only once in a list where every other element appears twice.

    Args:
        nums (List[int]): A list of integers where exactly one
        element appears once and all others appear twice.

    Returns:
        int: The single non-repeated element.
    """
    ans = 0
    repeated = set()
    for num in nums:
        if num in repeated:
            ans -= num
        else:
            ans += num
            repeated.add(num)
    return ans

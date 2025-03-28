# Time complexity is O(h * n) in the worst case where h and n are the lengths of haystack and needle, with O(1) constant space.
def first_occurrence(haystack: str, needle: str) -> int:
    """
    Finds the first occurrence of a substring (needle) in a string (haystack).

    Args:
        haystack (str): The string to search in
        needle (str): The substring to search for

    Returns:
        int: The index of the first occurrence of needle in haystack, or -1 if not found
    """
    needle_len = len(needle)
    haystack_len = len(haystack)
    fst_char = needle[0]
    index = 0
    while index + needle_len <= haystack_len:
        if haystack[index] == fst_char:
            index_temp = index
            length = 0
            for i in range(needle_len):
                if needle[i] == haystack[index_temp + i]:
                    length += 1
            if length == needle_len:
                return index
        index += 1
    return -1

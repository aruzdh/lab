def can_construct(ransom_note: str, magazine: str) -> bool:
    """
    Determines if a ransom note can be constructed from a given magazine string.

    Args:
        ransom_note (str): The string representing the ransom note to construct
        magazine (str): The string representing available characters from the magazine

    Returns:
        bool: True if the ransom note can be constructed from the magazine, False otherwise
    """
    letters = {}
    for char in magazine:
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1

    for char in ransom_note:
        if char not in letters or letters[char] == 0:
            return False
        letters[char] -= 1

    return True

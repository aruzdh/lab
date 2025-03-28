def square_digits(num):
    """
    Calculates the sum of squares of digits in a number.

    Args:
        num: An integer whose digits will be squared and summed

    Returns:
        int: The sum of squares of all digits in the input number
    """
    sum_sq = 0
    while num:
        digit = num % 10
        num //= 10
        sum_sq += digit * digit
    return sum_sq


# Time complexity is O(log n * d) where n is the input number and d is the number of digits in each step, with O(log n) space for the set of seen numbers.
def is_happy(n: int) -> bool:
    """
    Determines if a number is a happy number.
    A happy number is a number which eventually reaches 1 when replaced by
    the sum of the square of each digit, while unhappy numbers enter a cycle.

    Args:
        n (int): The number to check for happiness

    Returns:
        bool: True if the number is happy (reaches 1), False if it enters a cycle
    """
    numbers = set()
    sq_sum = n
    while sq_sum != 1:
        sq_sum = square_digits(sq_sum)
        if sq_sum in numbers:
            return False
        numbers.add(sq_sum)
    return True

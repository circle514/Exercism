"""Solution to the total number of grains on a chessboard given that square n has 2^n grains on it with 1 <= n <= 64"""

def square(number):
    """
    Calculate number of grains on a numbered square given a number within 1 and 64 (inclusive)

    Args:
        number (int): a number between 1 and 64 (inclusive)

    Returns:
        int: the number of grains on that square

    Raises:
        ValueError: if number is less than 1 or greater than 64 (inclusive)
    
    """
    if (number < 1 or number > 64):
        raise ValueError("square must be between 1 and 64")
    return 1 << number - 1


def total():
    """
    Calculate total number of grains on the chessboard

    Returns:
        total number of grains on the chessboard
    
    """
    return (1 << 64) - 1

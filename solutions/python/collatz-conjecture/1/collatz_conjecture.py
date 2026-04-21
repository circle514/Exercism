"""
    Count the steps given a number and running it through the collatz conjecture 
"""
def steps(number):
    """
        Count the steps given a number and running it through the collatz conjecture 

        Params: 
            Number: (int) the number to be plugged into the collatz conjecture

        Returns:
            Count: (int) the number of steps starting fron the first to when the number becomes 1 (inclusive)
    """
    count = 0
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    while number != 1 and number > 0:
        if number % 2 == 0:
            number /= 2
            count += 1
        else:
            number = 3 * number + 1
            count += 1
    return count

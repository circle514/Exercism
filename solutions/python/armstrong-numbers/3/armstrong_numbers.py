"""
    Check if a number is an armstrong number

    An armstrong number is a number that each digit raised to the number of digits all added up together equates to the number

    153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
    so 153 is an armstrong number
"""
def is_armstrong_number(number):
    """
        Oh my god you want me to write more? Fine

        Params:
            Number: (int) What do you think it is genius?

        Returns:
            Boolean: armstrong number or not??
    
    """
    str_num = str(number)
    power = len(str_num)
    result = 0
    for num in str_num:
        result += int(num) ** power

    return result == number
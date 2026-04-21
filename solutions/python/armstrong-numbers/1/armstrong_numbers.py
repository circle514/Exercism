def is_armstrong_number(number):
    str_num = str(number)
    power = len(str_num)
    result = 0
    for num in str_num:
        result += int(num) ** power

    return result == number
    

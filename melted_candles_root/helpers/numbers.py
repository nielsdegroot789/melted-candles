
def integer_with_point_to_decimal(num):
    separated_number = str(num).split('.')
    return separated_number[0] + separated_number[1]

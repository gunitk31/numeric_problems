def get_reverse(number):
    """Reverses the given number.

            Args
                number (int)
                    The number to reverse

            Returns
                Int: An integer value which represents the reverse of the given number"""
    rev_num_digits = []

    while number != 0:
        rev_num_digits.append(str(number % 10))
        number = number // 10

    rev_num = int(''.join(rev_num_digits))

    return rev_num


def is_palindrome_num(number):
    """Checks whether the given number is palindrome.

        Args
            number (int)
                The number to evaluate

        Returns
            Boolean: A boolean value indicating whether the given number is palindrome"""
    if number == get_reverse(number):
        return True
    else:
        return False


def get_largest_palindrome_product(number_length):
    """Calculates the largest palindrome number which is the product of 2 numbers of the given length.

            Args
                number_length (int)
                    The length of the 2 numbers whose product must be the largest palindrome

            Returns
                Int: The largest palindrome number which is the product of 2 numbers of the given length"""
    upper_limit = 9
    lower_limit = 1
    while number_length > 1:
        upper_limit = upper_limit*10 + 9
        lower_limit = lower_limit*10
        number_length -= 1

    for i in range(upper_limit,lower_limit,-1):
        for j in range(upper_limit,lower_limit,-1):
            product = i * j
            if is_palindrome_num(product):
                return product, i, j
        upper_limit -= 1


if __name__ == '__main__':
    print(get_largest_palindrome_product(3))

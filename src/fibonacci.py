def generate_fibonacci(sequence_length=2, starting_point=0):
    """Generates the fibonacci series between defined starting point and ending point.

    Args
        ending_point (int)
            Represents the last number in the generated fibonacci series

        starting_point (0 or 1)
            Represents the starting point of the generated fibonacci series, defaults to 0

    Returns
        List: The return value is a list containing the generated fibonacci series"""

    if starting_point not in [0, 1]:
        raise TypeError('Invalid Starting Point\nThe starting point of a fibonacci series can either be 0 or 1')

    first = starting_point
    second = starting_point + 1
    sum_of_last_two_numbers = first + second
    fibonacci_list = []

    if sequence_length == 1:
        fibonacci_list = [first]
    elif sequence_length > 1:
        fibonacci_list = [first, second]
        while len(fibonacci_list) != sequence_length:
            fibonacci_list.append(sum_of_last_two_numbers)
            sum_of_last_two_numbers = fibonacci_list[-2] + fibonacci_list[-1]

    return fibonacci_list


if __name__ == '__main__':
    help(generate_fibonacci)

    print(generate_fibonacci())
    print(generate_fibonacci(10))
    print(generate_fibonacci(10, 1))
    print(generate_fibonacci(10, 5))

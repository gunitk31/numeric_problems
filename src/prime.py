def is_prime(x):
    """
    Evaluates a given number to confirm if it is prime
    :param x: An integer value indicating the number to be evaluated
    :return: A boolean value indicating whether the given number is prime or not
    """

    if x < 2:
        return False
    elif x == 2:
        return True
    elif x != 2 and x % 2 == 0:
        return False
    else:
        for i in range(2, x):
            if x % i == 0:
                return False
        else:
            return True


def generate_next_prime(x):
    """
    Generate the next prime number after the given number
    :param x: An integer value indicating the last prime number that was generated
    :return: An integer value containing the next prime number that gets generated
    """
    x += 1
    while not is_prime(x):
        x += 1
    return x


def generate_prime_sequence(length=1):
    """
    Generates a sequence of prime numbers
    :param length: An integer value indicating the length of the generated sequence
    :return: A generator of the given length containing a sequence of prime numbers
    """

    x = 2
    i = 0

    while i < length:
        if is_prime(x):
            i += 1
            yield x
        x += 1


def gen_prime_factors(x):
    """
    Generate prime factors of a given number
    :param x: An integer value indicating the number whose prime factors need to be generated
    :return: An list of prime factors of the given number
    """

    prime_factors = []

    if x in [0, 1]:
        raise TypeError(f"The number {x} has no prime factors")
    else:
        prime_number = 2
        while not is_prime(x):
            if x % prime_number == 0:
                prime_factors.append(prime_number)
                x = int(x / prime_number)
            else:
                prime_number = generate_next_prime(prime_number)
        else:
            prime_factors.append(x)

    return prime_factors


if __name__ == '__main__':
    print(is_prime(5))
    print(is_prime(10))
    print(is_prime(17))
    print(is_prime(512))
    print(generate_next_prime(5))
    print(generate_next_prime(7))
    print(generate_next_prime(53))
    print(generate_prime_sequence())
    print(generate_prime_sequence(10))
    print(list(generate_prime_sequence(11)))
    print(gen_prime_factors(6))
    print(gen_prime_factors(77))
    print(gen_prime_factors(1034))
    print(gen_prime_factors(1012342222))

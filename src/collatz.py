def generate_collatz(starting_point=1):
    """Generates the collatz sequence between a starting point and 1.

    Args
        starting_point (int)
            Represents the starting point of the generated collatz sequence

    Returns
        List: The return value is a list containing the generated collatz sequence"""

    collatz_seq = [starting_point]

    while starting_point > 1:
        if starting_point % 2 == 0:
            starting_point = int(starting_point/2)
            collatz_seq.append(starting_point)
        else:
            starting_point = (3*starting_point) + 1
            collatz_seq.append(starting_point)

    return collatz_seq


if __name__ == '__main__':
    print(generate_collatz(13))
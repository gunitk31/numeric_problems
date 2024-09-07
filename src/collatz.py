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

    return len(collatz_seq), collatz_seq


def gen_largest_collatz_seq(max_starting_point=1000000):
    """Generates the largest collatz sequence under a defined maximum starting point.

    Args
        max_starting_point (int)
            Represents the maximum starting point that we want to generate the largest collatz sequence under

    Returns
        List: The return value is a list containing the largest collatz sequence under a defined maximum seq number"""

    largest_collatz_seq = []

    for starting_point in range(1,max_starting_point + 1):
        collatz_seq = generate_collatz(starting_point)[1]

        if len(collatz_seq) > len(largest_collatz_seq):
            largest_collatz_seq = collatz_seq

    return len(largest_collatz_seq), largest_collatz_seq


if __name__ == '__main__':
    print(generate_collatz(13))
    print(gen_largest_collatz_seq(20))
    print(gen_largest_collatz_seq())

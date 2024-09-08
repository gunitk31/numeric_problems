import prime
import fibonacci
import collatz
import palindrome

go_on: str = "Y"

while go_on == "Y":
    print("-------------------------------------------------")
    print("1. Generate Fibonacci Series")
    print("2. Generate a Prime Number")
    print("3. Generate a Sequence of Prime Number")
    print("4. Generate Prime Factors of a Given Number")
    print("5. Generate a Collatz Sequence")
    print("6. Generate the largest Collatz Sequence under a defined number")
    print("7. Generate the largest palindrome product of 2 numbers")
    print("0. Quit")
    print("-------------------------------------------------\n")

    choice: int = int(input("Pick a problem from the above list "))

    if choice == 0:
        break

    elif choice == 1:
        continue_gen = "Y"

        while continue_gen == "Y":

            starting_point_int = 0

            length = int(input("What is your preferred length for the fibonacci series that you want to generate? "))
            starting_point = input("Do you want to start your fibonacci sequence with 0 or 1? (Optional: 0/1) ")

            if starting_point != "":
                starting_point_int = int(starting_point)

            if starting_point_int not in [0, 1]:
                print(f"Starting point of a fibonacci sequence can either be 0 or 1")
                print(f"{starting_point_int} is not a valid starting point")
                print("Resetting starting point to 0...\n")
                starting_point_int = 0

            fibonacci_seq = fibonacci.generate_fibonacci(length, starting_point_int)

            print(f"Fibonacci Sequence -----> {fibonacci_seq}")

            continue_gen = "Dummy"
            while continue_gen not in ["Y", "N"]:
                continue_gen = input("Do you want to continue? (Y/N) ")
                continue_gen = continue_gen[0].upper()
                if continue_gen not in ["Y", "N"]:
                    print("Invalid Answer! Please try again...")

    elif choice == 2:
        prime_num: int = 2
        print(f'The smallest prime number is {prime_num}.')

        generate_next = input("Do you want to generate the next prime number? (Y/N) ")
        generate_next = generate_next[0].upper()

        while generate_next == "Y":
            prime_num = prime.generate_next_prime(prime_num)
            print(f"The next prime number is {prime_num}")

            generate_next = "Dummy"
            while generate_next not in ["Y", "N"]:
                generate_next = input("Do you want to generate the next prime number? (Y/N) ")
                generate_next = generate_next[0].upper()
                if generate_next not in ["Y", "N"]:
                    print("Invalid Answer! Please try again...")

    elif choice == 3:
        continue_gen = "Y"

        while continue_gen == "Y":
            length = int(input("How many prime numbers do you want to generate? "))
            prime_seq = list(prime.generate_prime_sequence(length))
            print(f"Prime Sequence -----> {prime_seq}")

            continue_gen = "Dummy"
            while continue_gen not in ["Y", "N"]:
                continue_gen = input("Do you want to continue? (Y/N) ")
                continue_gen = continue_gen[0].upper()
                if continue_gen not in ["Y", "N"]:
                    print("Invalid Answer! Please try again...")

    elif choice == 4:
        continue_gen = "Y"

        while continue_gen == "Y":
            x = int(input("Enter the number whose prime factors you want to generate? "))
            prime_fac_seq = prime.gen_prime_factors(x)
            print(f"Prime Sequence -----> {prime_fac_seq}")

            continue_gen = "Dummy"
            while continue_gen not in ["Y", "N"]:
                continue_gen = input("Do you want to continue? (Y/N) ")
                continue_gen = continue_gen[0].upper()
                if continue_gen not in ["Y", "N"]:
                    print("Invalid Answer! Please try again...")

    elif choice == 5:
        continue_gen = "Y"

        while continue_gen == "Y":
            starting_point = int(input("What do you want as the starting point of your collatz sequence? "))

            if starting_point < 1:
                print(f"Starting point of a collatz sequence can either be 0 or 1")
                print(f"{starting_point} is not a valid starting point")

            else:
                collatz_seq_len, collatz_seq = collatz.generate_collatz(starting_point)
                print(f"Collatz Sequence -----> {collatz_seq}")
                print(f"Length of the collatz sequence -----> {collatz_seq_len}")

            continue_gen = "Dummy"
            while continue_gen not in ["Y", "N"]:
                continue_gen = input("Do you want to continue? (Y/N) ")
                continue_gen = continue_gen[0].upper()
                if continue_gen not in ["Y", "N"]:
                    print("Invalid Answer! Please try again...")

    elif choice == 6:
        continue_gen = "Y"

        while continue_gen == "Y":
            max_starting_point = int(input("Under which number do you want to generate the largest collatz sequence? "))

            if max_starting_point < 1:
                print(f"Maximum starting point of a collatz sequence must be greater than or equal to 1")
                print(f"{max_starting_point} is not a valid starting point")

            else:
                largest_collatz_seq_len, largest_collatz_seq = collatz.gen_largest_collatz_seq(max_starting_point)
                print(f"Largest collatz Sequence under {max_starting_point} -----> {largest_collatz_seq}")
                print(f"Length of largest collatz sequence under {max_starting_point} -----> {largest_collatz_seq_len}")

            continue_gen = "Dummy"
            while continue_gen not in ["Y", "N"]:
                continue_gen = input("Do you want to continue? (Y/N) ")
                continue_gen = continue_gen[0].upper()
                if continue_gen not in ["Y", "N"]:
                    print("Invalid Answer! Please try again...")

    elif choice == 7:
        continue_gen = "Y"

        while continue_gen == "Y":
            number_length = int(input("What do you want as the length of the 2 numbers? "))

            if number_length < 1:
                print(f"Maximum length of number must be greater than or equal to 1")
                print(f"{number_length} is not a valid starting point")

            else:
                product, num1, num2 = palindrome.get_largest_palindrome_product(number_length)
                print(f"Largest Palindrome Product of 2 numbers of length {number_length} -----> {product}")
                print(f"The number {product} is the product of the 2 numbers, {num1} and {num2}")

            continue_gen = "Dummy"
            while continue_gen not in ["Y", "N"]:
                continue_gen = input("Do you want to continue? (Y/N) ")
                continue_gen = continue_gen[0].upper()
                if continue_gen not in ["Y", "N"]:
                    print("Invalid Answer! Please try again...")

    else:
        print("Invalid Choice! Try Again...")

    go_on = "Dummy"
    while go_on not in ["Y", "N"]:
        go_on = input("Do you want to choose a different puzzle? (Y/N) ")
        go_on = go_on[0].upper()
        if go_on not in ["Y", "N"] :
            print("Invalid Answer! Please try again...")

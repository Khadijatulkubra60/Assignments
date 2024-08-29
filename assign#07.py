def is_prime(num):
    """Checks if the number is prime."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i == 0 or num % (i + 2) == 0:
        return False
    i += 6
    return True

def main():
    name = input('What is your name?')
    print(f"Hello, {name}! Lets explore your favorite numbers.")

    numbers = []
    for j in range(3):
        num = int(input(f"Enter your {j + 1} favorite number: "))
        numbers.append(num)

    even_odd_numbers = [(num, "even" if num % 2 == 0 else "odd") for num in numbers]

    print("\nLets see what your numbers can do. ")
    for num in numbers:
        print(f"{num} squared is {num ** 2}")

    sum_of_numbers = sum(numbers)
    print(f"\nThe sum of your numbers is: {sum_of_numbers}")
    print("That's a great number! Keep exploring!")

    if is_prime(sum_of_numbers):
        print(f"\nAmazing! the sum of your numbers, {sum_of_numbers}, is a prime number!")
    else:
        print(f"\nInteresting. The sum of your numbers, {sum_of_numbers}, is not a prime number.")

if __name__ == "__main__":
    main()
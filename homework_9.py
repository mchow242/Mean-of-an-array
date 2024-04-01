def main():
    # Ask the user to enter 5 numbers
    numbers = []
    for i in range(1, 6):
        number = float(input(f"number {i}: "))
        numbers.append(number)

    # Calculate the arithmetic mean
    total = 0
    for num in numbers:
        total += num
    mean = total / len(numbers)

    # Print the result
    print(f"The mean of {numbers} is {mean:.2f}")

if __name__ == "__main__":
    main()

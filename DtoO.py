def decimal_to_octal(decimal_num):
    try:
        # Check if the input is a negative number
        is_negative = False
        if decimal_num < 0:
            is_negative = True
            decimal_num = abs(decimal_num)

        # Separate the integer and fractional parts
        integer_part = int(decimal_num)
        fractional_part = decimal_num - integer_part

        # Convert the integer part to octal
        octal_integer = oct(integer_part)[2:]

        # Convert the fractional part to octal (limit to 4 digits)
        octal_fractional = ''
        for _ in range(4):
            fractional_part *= 8
            octal_digit = int(fractional_part)
            octal_fractional += str(octal_digit)
            fractional_part -= octal_digit

        # Combine the integer and fractional parts
        octal_representation = octal_integer
        if octal_fractional:
            octal_representation += '.' + octal_fractional

        # Add a negative sign if necessary
        if is_negative:
            octal_representation = '-' + octal_representation

        return octal_representation
    except ValueError:
        return "Error: Invalid input. Please enter a valid decimal number."

try:
    # Get the decimal input from the user
    decimal_num = float(input("Enter a decimal number: "))

    # Convert the decimal number to its octal representation
    octal_num = decimal_to_octal(decimal_num)

    # Print the octal representation
    print(f"The octal representation of {decimal_num} is: {octal_num}")
except ValueError:
    print("Error: Invalid input. Please enter a valid decimal number.")

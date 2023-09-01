def decimal_to_hexadecimal(decimal_num):
    try:
        # Check if the input is a negative number
        is_negative = False
        if decimal_num < 0:
            is_negative = True
            decimal_num = abs(decimal_num)

        # Separate the integer and fractional parts
        integer_part = int(decimal_num)
        fractional_part = decimal_num - integer_part

        # Convert the integer part to hexadecimal and capitalize it
        hexadecimal_integer = hex(integer_part)[2:].upper()

        # Convert the fractional part to hexadecimal (limit to 4 digits)
        hexadecimal_fractional = ''
        for _ in range(4):
            fractional_part *= 16
            hexadecimal_digit = int(fractional_part)
            hexadecimal_fractional += hex(hexadecimal_digit)[2:].upper()
            fractional_part -= hexadecimal_digit

        # Combine the integer and fractional parts
        hexadecimal_representation = hexadecimal_integer
        if hexadecimal_fractional:
            hexadecimal_representation += '.' + hexadecimal_fractional

        # Add a negative sign if necessary
        if is_negative:
            hexadecimal_representation = '-' + hexadecimal_representation

        return hexadecimal_representation
    except ValueError:
        return "Error: Invalid input. Please enter a valid decimal number."

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

def decimal_to_binary(decimal_num):
    try:
        # Convert the decimal number to its IEEE 754 binary representation
        binary_representation = ''
        if decimal_num >= 0:
            sign_bit = '0'
        else:
            sign_bit = '1'
            decimal_num = -decimal_num

        integer_part = int(decimal_num)
        binary_representation += bin(integer_part)[2:] + '.'

        fractional_part = decimal_num - integer_part
        for _ in range(4):  # Limit to 4 digits after the decimal point
            fractional_part *= 2
            bit = '1' if fractional_part >= 1 else '0'
            binary_representation += bit
            fractional_part -= int(fractional_part)

        return sign_bit + binary_representation
    except ValueError:
        return "Error: Invalid input. Please enter a valid decimal number."
try:
    # Get the decimal input from the user
    decimal_num = float(input("Enter a decimal number: "))

    # Ask the user for the conversion type
    conversion_type = int(input("------------------------------\n"
                                "Choose the conversion type:\n"
                                 "2 for Binary\n"
                                 "10 for Octal\n"
                                 "16 for Hexadecimal\n"
                                 "------------------------------\n"
                                 "Enter your choose according to the given Numbers given above:- "))

    if conversion_type == 2:
        binary_num = decimal_to_binary(decimal_num)
        print(f"The binary representation of {decimal_num} is: {binary_num}")
    elif conversion_type == 10:
        octal_num = decimal_to_octal(decimal_num)
        print(f"The octal representation of {decimal_num} is: {octal_num}")
    elif conversion_type == 16:
        hexadecimal_num = decimal_to_hexadecimal(decimal_num)
        print(f"The hexadecimal representation of {decimal_num} is: {hexadecimal_num}")
    else:
        print("Invalid conversion type. Please enter 2, 10, or 16.")
except ValueError:
    print("Error: Invalid input. Please enter a valid decimal number.")

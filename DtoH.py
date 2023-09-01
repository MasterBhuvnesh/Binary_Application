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

try:
    # Get the decimal input from the user
    decimal_num = float(input("Enter a decimal number: "))

    # Convert the decimal number to its hexadecimal representation
    hexadecimal_num = decimal_to_hexadecimal(decimal_num)

    # Print the  hexadecimal representation
    print(f"The hexadecimal representation of {decimal_num} is: {hexadecimal_num}")
except ValueError:
    print("Error: Invalid input. Please enter a valid decimal number.")

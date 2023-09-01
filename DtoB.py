def float_to_binary(decimal_num):
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

    # Convert the decimal number to its binary representation
    binary_num = float_to_binary(decimal_num)

    # Print the binary representation
    print(f"The binary representation of {decimal_num} is: {binary_num}")
except ValueError:
    print("Error: Invalid input. Please enter a valid decimal number.")


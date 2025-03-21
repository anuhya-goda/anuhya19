def binary_to_decimal(binary: str) -> int:

    decimal = 0
    power = 0
    for digit in reversed(binary):  # Start from the rightmost digit
        if digit == '1':
            decimal += 2 ** power
        power += 1
    return decimal


def octal_to_decimal(octal: str) -> int:
    decimal = 0
    power = 0
    for digit in reversed(octal):
        decimal += int(digit) * (8 ** power)
        power += 1
    return decimal


def hex_to_decimal(hex_num: str) -> int:
    
    decimal = 0
    power = 0
    hex_num = hex_num.upper()  
    for digit in reversed(hex_num):
        if '0' <= digit <= '9':
            value = int(digit)
        elif 'A' <= digit <= 'F':
            value = ord(digit) - ord('A') + 10
        else:
            raise ValueError("Invalid hexadecimal number!")
        decimal += value * (16 ** power)
        power += 1
    return decimal


#  Code
if __name__ == "__main__":
    binary = input("Enter a binary number: ")
    print("Decimal equivalent:", binary_to_decimal(binary))

    octal = input("Enter an octal number: ")
    print("Decimal equivalent:", octal_to_decimal(octal))

    hex_num = input("Enter a hexadecimal number: ")
    print("Decimal equivalent:", hex_to_decimal(hex_num))

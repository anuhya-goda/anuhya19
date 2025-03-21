def hexadecimal_to_other(hex_num):
    decimal = int(hex_num, 16)

    binary = bin(decimal) 
    octal = oct(decimal)   

    print(f"Decimal: {decimal}")
    print(f"Binary: {binary}")
    print(f"Octal: {octal}")

hex_input = input("Enter a hexadecimal number: ")

hexadecimal_to_other(hex_input)

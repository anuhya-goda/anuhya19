def binary_to_other(binary_num):
    
    decimal = int(binary_num, 2)
    
   
    octal = oct(decimal)
     
    hexadecimal = hex(decimal).upper()  
   
    print(f"Decimal: {decimal}")
    print(f"Octal: {octal}")
    print(f"Hexadecimal: {hexadecimal}")


binary_input = input("Enter a binary number: ")

binary_to_other(binary_input)
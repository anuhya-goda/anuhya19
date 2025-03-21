def octal_to_other(octal_num):
  
    decimal = int(octal_num, 8)

  
    binary = bin(decimal) 
    hexadecimal = hex(decimal).upper() 
   
    print(f"Decimal: {decimal}")
    print(f"Binary: {binary}")
    print(f"Hexadecimal: {hexadecimal}")


octal_input = input("Enter an octal number: ")

octal_to_other(octal_input)
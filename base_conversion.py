import math

ALLOWED_BASES = [2, 8, 16]

def to_base(base, n):
    # throw an error in user did not entered the number
    if n == "":
        raise Exception(f"ERROR: You have not entered a number.") 
    
    # throw error if did not entered integer
    if n.isdigit():
        n = int(n)
    else:
        raise Exception(f"{n} is not a decimal")
    
    n = int(n)
    if base not in ALLOWED_BASES:
        raise Exception(f"ERROR: You entered base {base}, the supported bases are {ALLOWED_BASES}.")
    reminders_array = []
    base_num = ""
    while n/base > 0:
        rem = n%base
        if rem > 9 and rem < 36:
            charA = 65
            rem = chr(charA+rem-10)

        reminders_array.append(rem)
        n = math.floor(n/base)
    while len(reminders_array) > 0:
        base_num+=str(reminders_array.pop(len(reminders_array)-1))
    return base_num
  

def to_decimal(base, n):
    # throw an error in user did not entered the number
    if n == "":
        raise Exception(f"ERROR: you did not entered any number") 
    # throw an error if user trying to enter bases other than 2, 8, or 16
    if base not in ALLOWED_BASES:
        raise Exception(f"ERROR: You entered base {base}, the supported bases are {ALLOWED_BASES}.")
    
    # result variable allows to assemble the final number
    result = 0

    # index variable follow the opposite direction to allow to convert number from base to decimal
    index = len(n)-1

    # unsupported_characters variable holds characters that not allowed for the number with the base user entered
    unsupported_characters = set()

    # iterate the characters
    for x in n:
        if ord(x) >= 48 and ord(x) <= 57:
            #  modify string with digit character to integer for future calculation 
            x=int(x)
            if x >= base:
                # character cannot be more or equal than base
                raise Exception(f"ERROR: The number {n} is not valid for base {base}.")
        elif ord(x.upper()) >= 65 and ord(x.upper()) <= 70 and base == 16:
            #  modify string with letters "A,B,C,D,E" to correct digit if the vase 16 
            x=x.upper()
            x=ord(x)-55
        else:
            # if base does not support character - include this character to the unsupported_characters set
            unsupported_characters.add(x)

        # if no unsupported_characters - calculate result for each character
        # if unsupported_characters variable contain any character - this calculation omitted, 
        # and the loop only create full set of unsupported_characters
        if len(unsupported_characters) == 0:
            result += x*pow(base, index)
            index-=1
    # throw error if user trying to convert wrong integer
    if len(unsupported_characters) > 0:
        raise Exception(f"ERROR: You entered number '{n}', for base '{base}' this number contains the unsupported characters: '{', '.join(unsupported_characters)}'.")
    return result
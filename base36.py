# to_base_36
# research solution for this
# Keep track of values 0-9, A-Z, as 0-36

# input number -> divide by 36 (save number for next iteration), % 36 (convert to 0-Z format, add to beginning of output string) 
# can get divide and mod with divmod() method

# Divide the number by 36.
# Get the integer quotient for the next iteration.
# Get the remainder for the hex digit.
# Repeat the steps until the quotient is equal to 0.
alphabet = {
    "0" : "0",
    "1" : "1",
    "2" : "2",
    "3" : "3",
    "4" : "4",
    "5" : "5",
    "6" : "6",
    "7" : "7",
    "8" : "8",
    "9" : "9",
    "10" : "A",
    "11" : "B",
    "12" : "C",
    "13" : "D",
    "14" : "E",
    "15" : "F",
    "16" : "G",
    "17" : "H",
    "18" : "I",
    "19" : "J",
    "20" : "K",
    "21" : "L",
    "22" : "M",
    "23" : "N",
    "24" : "O",
    "25" : "P",
    "26" : "Q",
    "27" : "R",
    "28" : "S",
    "29" : "T",
    "30" : "U",
    "31" : "V",
    "32" : "W",
    "33" : "X",
    "34" : "Y",
    "35" : "Z"
}

key_list = list(alphabet.keys())
val_list = list(alphabet.values())

r = 29234652

def to_base_36(r, result):
    result += alphabet[str(divmod(r, 36) [1])]  # mod remainder (converted to base36 value)
    if divmod(r, 36) [0] != 0:
        to_base_36(divmod(r, 36) [0], result) # quotient (pushed back to method)
    else:
        print(result[::-1])


to_base_36(r, "")

def to_int(r):
    y, result = 0, 0
    for x in list(str(r))[::-1]: # for breaking up the base36 into components for converting
        result += int(key_list[val_list.index(x)]) * 36 ** y
        y += 1
    print(result)
# Similar method to converting from haxadecimal/binary to integer
# Reverse string, break for each element in string - convert to numerical value - *36^[x] + ...
to_int("FUCKYOU")

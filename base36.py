# to_base_36
# research solution for this
# Keep track of values 0-9, A-Z, as 0-36

# input number -> divide by 36 (save number for next iteration), % 36 (convert to 0-Z format, add to beginning of output string) 
# can get divide and mod with divmod() method
r = 73
def to_base_36(r):
    print("Mod remainder: " + str(divmod(r, 36) [1])) # mod remainder (converted to base36 value)
    print("Quotient (floor): " + str(divmod(r, 36) [0])) # quotient (pushed back to method)
to_base_36(r)

# to_int
# Similar method to converting from haxadecimal/binary to integer
# Reverse string, break for each element in string - convert to numerical value - *36^[x] + ...
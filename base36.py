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

def to_base_36(r, result):
    result += alphabet[str(divmod(r, 36) [1])]  
    if divmod(r, 36) [0] != 0:
        to_base_36(divmod(r, 36) [0], result) 
    else:
        print(result[::-1])

def to_int(r):
    y, result = 0, 0
    for x in list(str(r))[::-1]: 
        result += int(key_list[val_list.index(x)]) * 36 ** y
        y += 1
    print(result)

# Convert integer to base36
to_base_36(11168434984638296100531098218969554919276774, "")
# Convert word to integer
to_int("ANTIDISESTABLISHMENTARIANISM")

from itertools import chain
import string

alphabet = { i : str(c) for i,c in enumerate(chain(range(10), string.ascii_uppercase)) }
inv_alphabet = { val : key for key, val in alphabet.items() }

divmod36 = lambda r: divmod(r, 36)

def to_base_36(r):
    def helper(r):
        if not r: return
        q, r = divmod36(r)
        yield from helper(q)
        yield alphabet[r]
    return ''.join(helper(r))

def to_int(r):
    return sum(inv_alphabet[x] * 36 ** i for i, x in enumerate(reversed(str(r))))

# Convert integer to base36
print(to_base_36(11168434984638296100531098218969554919276774))
# Convert word to integer
print(to_int("ANTIDISESTABLISHMENTARIANISM"))

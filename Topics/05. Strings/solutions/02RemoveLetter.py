def remove_letter(letter, s):
    return s.replace(letter, '')

assert(remove_letter("a", "apple") == "pple")
assert(remove_letter("a", "banana") == "bnn")
assert(remove_letter("z", "banana") == "banana")
assert(remove_letter("i", "Mississippi") == "Msssspp")
assert(remove_letter("b", "") == "")
assert(remove_letter("b", "c") == "c")
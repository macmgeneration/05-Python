def mirror(s):
    result = s
    index = len(s) - 1
    while index >= 0:
        result += s[index]
        index -= 1
    return result

assert(mirror("good") == "gooddoog")
assert(mirror("Python") == "PythonnohtyP")
assert(mirror("") == "")
assert(mirror("a") == "aa")
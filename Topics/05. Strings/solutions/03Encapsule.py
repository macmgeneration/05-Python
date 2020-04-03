def count_letters(s, letter):
    count = 0
    for char in s:
        if char == letter:
            count += 1
    return count

print(count_letters("banana", 'a'))
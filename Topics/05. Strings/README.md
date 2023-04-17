# Strings

## Simple Exercises

* [w3schools/strings](https://www.w3schools.com/python/exercise.asp?filename=exercise_strings1)

## Exercises

1. Write a function that mirrors its argument:
    ``` python
    assert(mirror("good") == "gooddoog")
    assert(mirror("Python") == "PythonnohtyP")
    assert(mirror("") == "")
    assert(mirror("a") == "aa")
    ```
2. Write a function that removes all occurrences of a given letter from a string:
    ``` python
    assert(remove_letter("a", "apple") == "pple")
    assert(remove_letter("a", "banana") == "bnn")
    assert(remove_letter("z", "banana") == "banana")
    assert(remove_letter("i", "Mississippi") == "Msssspp")
    assert(remove_letter("b", "") == "")
    assert(remove_letter("b", "c") == "c")
    ```
3. Encapsule in a function named count_letters, and generalize it so that it accepts the string and the letter as arguments. Make the function return the number of characters, rather than print the answer. The caller should do the printing.
    ``` python
    fruit = "banana"
    count = 0
    for char in fruit:
        if char == "a":
            count += 1
    print(count)
    ```
4. Assign to a variable in your program a triple-quoted string that contains your favourite paragraph of text — perhaps a poem, a speech, instructions to bake a cake, some inspirational verses, etc.

    Write a function which removes all punctuation from the string, breaks the string into a list of words, and counts the number of words in your text that contain the letter “e”. Your program should print an analysis of the text like this:
    ``` python
    Your text contains 243 words, of which 109 (44.8%) contain an "e".
    ```
# Regular Expresions

## Exercises

1. Write a simple program to simulate the operation of the grep command on Unix. Ask the user to enter a regular expression and count the number of lines that matched the regular expression, in the file mbox.txt:
   ```cmd
   $ python grep.py
    Enter a regular expression: ^Author
    mbox.txt had 27 lines that matched ^Author

    $ python grep.py
    Enter a regular expression: ^X-
    mbox.txt had 14368 lines that matched ^X-

    $ python grep.py
    Enter a regular expression: java$
    mbox.txt had 4175 lines that matched java$
   ```
2. Write a program to look for lines of the pattern:
    ```cmd
    New Revision: 39772
    ```
   Extract the number from each of the lines using a regular expresion and the ```findall()``` method. Compute the average of the numbers and print out the average as an integer.
    ```cmd
    Enter file: mbox.txt
    Average: 38549

    Enter file: mbox-short.txt
    Average: 39756
    ```

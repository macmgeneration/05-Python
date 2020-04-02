# Iterations

## Simple Exercises

* [w3schools/whileloops](https://www.w3schools.com/python/exercise.asp?filename=exercise_while_loops1)
* [w3schools/forloops](https://www.w3schools.com/python/exercise.asp?filename=exercise_for_loops1)

## Exercises

* Write a program to count how many odd numbers are from 0 to number input from user.
* Sum up all the even numbers from 0 to number input from user.
* Write a program with this steps:
  * Request a number from user
  * Check is the last number is the largest number entered so far
  * Repeat until user input '#' text
  * Show largest number
* Write a simple guessing game:
  * Generate a random number between 0 and 1000, it's called hidden number
  * Request a number from user
  * Go indicanting the user if it is greater or less than the hidden number
  * Repeat until the user guesses the number
   ```python
   ## (hint: to generate random number)
   import random
   rng = random.Random()
   number = rng.randrange(1,1000)
   ```
  

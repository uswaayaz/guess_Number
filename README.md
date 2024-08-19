# guess_Number

This code is a simple number-guessing game where the player has to guess a randomly generated number between 1 and 100. Here's a step-by-step explanation of how the code works:

1. **Importing the Random Module**:
   ```python
   import random
   ```
   - The `random` module is imported to generate a random number. This module provides functions to perform random operations.

2. **Generating a Random Number**:
   ```python
   n = random.randint(1, 100)
   ```
   - `random.randint(1, 100)` generates a random integer between 1 and 100 (inclusive) and assigns it to the variable `n`. This is the number the player will try to guess.

3. **Initial Setup**:
   ```python
   a = -1
   guesses = 1
   ```
   - The variable `a` is initialized to `-1`. This is a placeholder to store the user's guess.
   - The variable `guesses` is initialized to `1`. This keeps track of the number of attempts the player has made to guess the correct number.

4. **Starting the Guessing Loop**:
   ```python
   while(a != n):
   ```
   - A `while` loop begins, which will continue running as long as the player's guess (`a`) is not equal to the random number (`n`). Since `a` is initially set to `-1` (which is not equal to `n`), the loop will always run at least once.

5. **Player's Guess Input**:
   ```python
   a = int(input("Enter the number: "))
   ```
   - The player is prompted to enter a number, and the input is converted to an integer and stored in the variable `a`.

6. **Checking the Guess**:
   ```python
   if(a > n):
       print("Lower number please")
       guesses += 1
   ```
   - If the player's guess (`a`) is greater than the random number (`n`), the program informs the player that they need to guess a lower number. The `guesses` counter is then incremented by 1.

   ```python
   elif(a < n):
       print("Higher number please")
       guesses += 1
   ```
   - If the player's guess (`a`) is less than the random number (`n`), the program informs the player to guess a higher number. Again, the `guesses` counter is incremented by 1.

7. **Correct Guess**:
   ```python
   print(f"You have guessed the number {n} correctly in {guesses} attempts")
   ```
   - When the player finally guesses the correct number, the `while` loop ends because `a` is now equal to `n`.
   - The program then prints a message congratulating the player, displaying the correct number and the total number of attempts it took to guess correctly.

### Summary
The game randomly selects a number between 1 and 100. The player is repeatedly prompted to guess the number, with hints provided if the guess is too high or too low. The game continues until the player guesses the correct number, at which point the total number of attempts is displayed.

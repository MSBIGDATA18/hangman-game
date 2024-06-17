# hangman-game
# Step 1: Import Libraries
- Start by importing the necessary libraries: tkinter for creating the graphical user interface and random for selecting a random word.
# Step 2 : Define a List of Words
- Create a list of words that will be used in the game. These words will be the ones the player has to guess.
# Step 3: Initialize the Main Tkinter Window
Set up the main window for the game, including giving it a title and setting its dimensions.
# Step 4: Create the User Interface Widgets
Add the necessary widgets to the window, such as labels, entry fields, buttons, and a canvas:
- A label to display the game title.
- An entry field where the player can input their guesses.
- A button that the player clicks to check their guess.
- A label to display the number of lives remaining.
- A canvas to draw the hangman figure


# Step 5: Define the Function to Draw the Hangman
- Create a function that draws parts of the hangman figure on the canvas as the player loses lives. This function updates the drawing based on the number of lives left.

# Step 6: Initialize the Chosen Word and Game Variables
- Randomly select a word from the list and initialize the variables for the game:

- The chosen word.
- A list to keep track of the correctly guessed letters (initially filled with underscores).
The number of lives the player has.
# Step 7: Define the Check Function
Create a function to check if the player's guess is in the chosen word:

- Update the guessed letters list if the guess is correct.
- Decrease the number of lives and draw the hangman if the guess is incorrect.
- Update the display of the guessed word.
- Check if the player has won or lost, and show an appropriate message.

# Step 8: Run the Tkinter Main Loop
- Finally, start the Tkinter main loop to run the game. This keeps the window open and responsive to user interactions.

By following these steps, you can create a functional Hangman game using Tkinter in Python. The game will allow players to input guesses, update the display with correct guesses, draw the hangman figure as incorrect guesses are made, and show win/loss messages based on the game's outcome.






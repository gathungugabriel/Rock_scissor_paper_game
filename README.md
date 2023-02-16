# Rock, Scissor, Paper Game
This is a simple Rock, Paper, Scissors game in which two players can choose from the options of rock, paper, or scissors. 
The game uses a set of if-else statements to determine the winner based on the combination of choices made by both players.
# Requirements
To run this game, you'll need Python 3 installed on your computer.
# How to play
1. Clone this repository to your local machine.
2. Open the command line and navigate to the repository's directory.
3. Run the `rps_game.py` file using the `python` command:
``` python rps_game.py ```
4. Follow the on-screen instructions to choose your options and determine the winner.

# How it works
The game starts by printing out the available options and then prompts the first
player to make a choice. The choice is validated, and the second player is also 
prompted to make a choice, which is also validated. Then, the function 
corresponding to the first player's choice is called to determine the winner of the game.

The three functions used to determine the winner for each possible combination of 
choices are `play_rock`, `play_scissors`, and `play_paper`. These functions take 
two arguments, representing the choices made by the two players, and use if-else 
statements to determine the winner based on the rules of the game. The function 
returns 1 if player 1 wins, 2 if player 2 wins, and 0 if it's a draw.

# Contributing
Feel free to fork this repository and make changes as needed. If you'd like to 
contribute to the project, please open a pull request with your suggested changes.

# License
This project is licensed under the **__MIT License__**.

# Acknowledgements
This project was inspired by __desire__ for  use of basic programming concepts like functions, 
conditional statements, and loops to create a working program!

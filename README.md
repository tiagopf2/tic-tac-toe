# Tic Tac Toe RAT

A deceptively simple terminal-based Tic Tac Toe game that hides a Remote Access Tool (RAT) underneath. While the user plays, the game secretly opens a backdoor, giving remote command-line access to an attacker.

>  This project is for **educational and ethical penetration testing only**. Do not use this on any system without explicit permission.


## How It Works

- **`tictactoe-clean.py`** runs the actual Tic Tac Toe game.
- On launch, it imports or silently executes **`backdoor-victim.py`**, which establishes a connection to the attacker's server.
- **`backdoor-server.py`** listens for the connection and gives the attacker a terminal to send commands and receive responses.


##  File Structure


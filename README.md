# Day 7 – Hangman Project 🪢💀

## Description
In this project, you build a classic **Hangman** game in Python. The player tries to guess a secret word letter by letter, with a limited number of attempts. A visual representation (ASCII art) shows the number of remaining lives.

## Features
- Word selection from a predefined word list  
- ASCII art for each stage of the game  
- Tracks guessed letters  
- Displays blanks and correct letters dynamically  
- Handles win and lose conditions

## Example Output
```
Welcome to
 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    
Guess a letter: 
a

  +---+
  |   |
  O   |
      |
      |
      |
=========

_________
The letter a was not in the word.
You have 5/6 lives left.
...
```

## Skills Learned
- Importing and using external modules (e.g., `hangman_art.py`, `hangman_words.py`)  
- Managing and updating lists (e.g., blanks replaced by correct guesses)  
- Conditional logic and control flow (`if`, `else`, `while`)  
- Loops for iteration  
- Indexing and comparison  
- ASCII formatting  
- Game loop and game state tracking

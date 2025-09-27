# 🪨📄✂️ Rock-Paper-Scissors CLI Game

This is a command-line Rock-Paper-Scissors game built in Python as part of Task 5 for the CODSOFT internship. It features a user-friendly interface, score tracking, and optional color-coded output using `colorama`.

## 🚀 Features

- **User Input**  
  Prompt to choose rock, paper, or scissors with input validation.

- **Computer Selection**  
  Random choice generated using Python's `random` module.

- **Game Logic**  
  Determines the winner based on classic rules:
  - Rock beats Scissors
  - Scissors beats Paper
  - Paper beats Rock

- **Result Display**  
  Shows both choices and announces win, lose, or tie.

- **Score Tracking**  
  Keeps track of user and computer scores across rounds.

- **Replay Option**  
  Allows the user to play multiple rounds until they choose to exit.

- **Color-Coded Feedback** *(Optional)*  
  Uses `colorama` to highlight results and choices.

## 🧰 Technologies Used

- Python 3
- `random` (built-in)
- `colorama` *(optional, for colored output)*

## 📦 Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

## ▶️ How to Run

Run the game using the following command:

```bash
python rps_game.py
```

## 🎥 Demo Video

Watch the Rock-Paper-Scissors CLI game in action:  
▶️ [Demo Video on LinkedIn](https://www.linkedin.com/posts/sai-gowtham-2220a7322_codsoft-python-cliapp-activity-7377661000419897344-MZ88?utm_source=share&utm_medium=member_android&rcm=ACoAAFGG-noBf6Ra_yXj5kk1v4eztQcMwVzOv9c)

This video demonstrates the actual **input/output flow** of the game:

- User is prompted to choose: `rock`, `paper`, or `scissors`
- Computer randomly selects its move
- Both choices are displayed
- Game logic determines the winner
- Result is shown: win, lose, or tie
- Score is updated and displayed
- User is asked: “Play another round? (y/n)”

The game runs in a loop until the user exits, with color-coded feedback and clean interaction.



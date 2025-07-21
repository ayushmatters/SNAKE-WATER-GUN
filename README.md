# SNAKE-WATER-GUN
...My First Project SNAKE WATER GUN Game...
# 🐍 Snake, Water, Gun Game

A simple terminal-based Python game inspired by Rock-Paper-Scissors, with a twist!  
Play against the computer by choosing **Snake**, **Water**, or **Gun** — and see who wins!

---

## 📌 Features

- Random computer moves using `random.choice()`
- User input validation
- Match result display (Win/Lose/Draw)
- Fully written in beginner-friendly Python

---

## 🚀 How to Run

1. **Clone this repository:**

```bash
git clone https://github.com/your-username/snake-water-gun-game.git
cd snake-water-gun-game
```

2. **Run the script:**

```bash
python snake_water_gun.py
```

> Make sure Python 3 is installed on your system.

---

## 🎮 Game Rules

| Player Move | Computer Move | Result         |
|-------------|----------------|----------------|
| Snake       | Water          | Player Wins    |
| Snake       | Gun            | Computer Wins  |
| Water       | Gun            | Player Wins    |
| Water       | Snake          | Computer Wins  |
| Gun         | Snake          | Player Wins    |
| Gun         | Water          | Computer Wins  |
| Same Choice | Same Choice    | Draw           |

---

## 💻 Sample Output

```plaintext
Your Turn (snake / water / gun): water
Computer Enters: gun
You Entered: water
You won, Computer lose
```

---

## 📂 File Structure

```
snake-water-gun-game/
├── snake_water_gun.py       # Python game logic
└── README.md                # Project overview (this file)
```

---

## 🧠 Concepts Used

- Python `random` module
- User input handling
- String methods
- Conditional statements

---


If you found this project helpful, consider giving it a ⭐ on GitHub to support the work!

# Password Cracker

This repository contains a collection of Python scripts that demonstrate different methods of brute-force password cracking through simulated attacks. 

> [!NOTE]
> These scripts require the user to input the target password to simulate the cracking process. They are meant for **educational and entertainment purposes** to demonstrate how brute-force algorithms and random string generation operate, rather than for practical password recovery.

## The Scripts

### 1. `password_cracker.py` (Random Guessing)
This script attempts to crack the provided password by repeatedly generating completely random strings of the exact same length. 
- **Method:** Purely random guessing.
- **Performance:** Very fast at generating guesses, but because it relies entirely on randomness, it might guess the same wrong combination multiple times and can theoretically take a very long time to stumble upon the correct password.

### 2. `cracker1.py` (Deterministic Brute-Force)
This script uses a systematic brute-force approach to guess the password. It utilizes Python's `itertools.product` to methodically test every single possible combination of characters (letters, numbers, and symbols) that matches the length of the given password.
- **Method:** Exhaustive combination testing.
- **Performance:** Guarantees that it will eventually find the password by trying every possibility exactly once. However, for longer passwords, the number of combinations grows exponentially, which can still take a significant amount of time.

### 3. `cracker2.py` (Alternate Brute-Force)
This script is identical in functionality to the optimized `cracker1.py`. It directly targets combinations of the exact length of the provided password to save time.

## Usage

To run any of the scripts, simply execute them with Python in your terminal:

```bash
python password_cracker.py
# OR
python cracker1.py
# OR
python cracker2.py
```

Then, follow the prompt to enter a password for the script to simulate cracking.

## Requirements

- Python 3.x
- No external dependencies are required.

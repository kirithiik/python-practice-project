# ATM Simulator (Python)

A console-based ATM simulation built using Python.
This project was created to practice core programming concepts along with basic file handling using JSON for data persistence.

## Features
- Create a bank account
- Deposit money
- Withdraw money with balance validation
- Check current balance
- View transaction history
- Persistent data storage using JSON (account data is saved and loaded)

## Concepts Used
- Functions and control flow
- Lists and dictionaries
- State management
- File handling with JSON
- `os.path.exists()` for safe file operations
- Input validation
- Menu-driven command line interface

## How It Works
- Account data is stored in a JSON file (`account.json`)
- When the program starts, it loads existing account data if available
- All changes (deposit, withdrawal) are saved immediately
- Data persists even after closing and reopening the program

## How to Run
1. Make sure Python is installed.
2. Run the program using:
   ```bash
   python atm_simulator.py

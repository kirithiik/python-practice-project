# Rule-Based Chatbot v1 (Python)

A simple rule-based chatbot built using Python.
The chatbot interacts with the user through the command line and responds to predefined intents using keyword matching.

## Features
- Responds to greetings (hi, hello)
- Answers "how are you"
- Tells the current time
- Explains what it can do using a help command
- Shares information about its creator
- Exits politely when the user says bye
- Handles unknown inputs gracefully

## Concepts Used
- Functions
- Conditional logic
- String processing
- Substring matching
- While loops
- Datetime module
- Program flow control

## How It Works
- The user enters a message
- The input is converted to lowercase for consistent matching
- The chatbot checks for keywords inside the input
- Based on the detected intent, an appropriate response is returned
- The conversation continues until the user types "bye"

## Example Commands
- hi
- hello there
- how are you
- time
- help
- who made you
- bye

## How to Run
1. Ensure Python is installed.
2. Run the program using:
   ```bash
   python chatbot_v1.py

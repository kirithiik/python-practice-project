# 🤖 Chatbot Quiz Hybrid (Python)

A command-line based chatbot-style quiz application built using Python.  
The chatbot interacts with the user in a conversational way and conducts a quiz using free-text answers instead of fixed options.

---

## 📌 Project Overview

This project combines basic chatbot interaction with quiz logic.  
The chatbot can understand simple user intents and respond accordingly.

---

## ✨ Features

- Conversational chatbot interface
- Free-text answer checking (keyword-based)
- Dynamic question addition during runtime
- Quiz score tracking
- Intent-based interaction (no menus)
- Graceful exit handling

---

## 🧠 Concepts Used

- Lists and dictionaries
- Functions and modular design
- String processing and keyword matching
- Loops and conditional logic
- Global state management
- Basic system design principles

---

## 🗂️ Data Structure

Questions are stored as a list of dictionaries:

```python
qa = [
    {
        "question": "What language is best for AI?",
        "answer": "python"
    }
]
 
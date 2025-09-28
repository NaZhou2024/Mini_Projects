
---
# ⏱ Countdown Timer Projects

A series of progressively enhanced countdown timer projects in Python, starting from a simple command-line script and evolving into a fully-featured GUI with logging capabilities.

---

## 📁 Project Overview

### 1️⃣ `RV2ZhouNa.py` — Basic Countdown Timer

A beginner-friendly script using a function called `countdown`:
- Takes user input in seconds.
- Counts down using `time.sleep()` and prints each second.
- Exits early when user presses `'x'` (via the `keyboard` library).
- Outputs a custom message when finished.

🔧 **Libraries used:** `time`, `keyboard`  

---

### 2️⃣ `CH9LastFirst.py` — Object-Oriented Countdown

Improved version using a class called `countdown`:
- Encapsulates logic inside methods: `Start()`, `Stop()`, and `TimeRemaining()`.
- Uses a private data field to monitor `'x'` key for early exit.
- Accepts user input for countdown duration.

🛠 **Libraries used:** `time`, `keyboard`  
🏗️ **Structured, modular, and ready for reuse.**

---

### 3️⃣ `CH12LastFirst.py` — Countdown with GUI

Adds a graphical interface using Tkinter:
- GUI shows countdown messages (customizable).
- Buttons for Start, Stop, and Reset.
- Clean design using class `stopwatch`.

🎨 **Optional customization:** Add colors, images, or use inheritance.  
📚 **Built on lessons from Chapter 10 & 11.**

---

### 4️⃣ `CH14LastFirst.py` — Advanced GUI + Logging

Fully-featured GUI timer with advanced functionality:
- Adds a Quit button with confirmation dialog.
- Logs all actions (start, stop, reset) to `log.txt`.
- Handles file errors with user-friendly dialogs.

🗂️ **Includes logging, file checks, and error handling.**  
💡 **Perfect capstone for learning GUI + I/O + user experience.**

---

## ▶️ How to Run

Each script can be run from the command line:

```bash
python filename.py

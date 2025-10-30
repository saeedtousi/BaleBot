# 🤖 BaleBot - Setup Guide for Students

Welcome! This repository contains a Python-based bot for the Bale messaging platform. Follow the steps below to install the required tools, set up your environment, and run the bot locally.

---

## 📦 Step 1: Install Git

To download this project from GitHub, you need Git installed on your system.

🔗 [Download Git for Windows](https://git-scm.com/install/windows)

During installation, accept the default settings.

---

## 🐍 Step 2: Install Python

If Python is not already installed:

🔗 [Download Python](https://www.python.org/downloads/)

Make sure to check **Add Python to PATH** during installation. Python 3.10 or higher is recommended.

---

## 📥 Step 3: Clone the Project

1. Create a folder where you want to store the project  
2. Right-click inside the folder and choose **Git Bash Here**  
3. Run the following command:

git clone https://github.com/saeedtousi/BaleBot.git
cd BaleBot

🧪 Step 4: Create and Activate a Virtual Environment
To isolate project dependencies:
python -m venv venv

Activate the virtual environment:
• 	On Windows:
.\venv\Scripts\activate

You should now see (venv) at the beginning of your terminal prompt.

📋 Step 5: Install Dependencies
With the virtual environment activated, install the required packages:
pip install -r requirements.txt

🚀 Step 6: Run the Bot
To start the bot:
python app\balebot_async.py

❗ Notes
• 	Ensure you have an active internet connection during installation
• 	If you encounter any errors, copy the error message and share it with your instructor
• 	The  (venv) folder is excluded from Git tracking via .gitignore

👨‍🏫 Author
Developed by saeedtousi for educational use by students.

# 🔐 Password Generator (Django)

A clean, beginner-friendly Django web app that generates secure, customizable passwords right from your browser.  
Built with Python + Django to demonstrate basic web app development, template rendering, and form handling.

---

## ✨ Features

- 🔢 Choose password **length**
- 🔡 Toggle character sets: **uppercase**, **lowercase**, **digits**, and **symbols**
- ⚙️ Fully server-side logic using Django views
- 🖥️ Simple, responsive interface

---

## 📦 Requirements

- **Python 3.9+**
- **Django 4.x+**
- (Optional) `python-dotenv` if you want to load environment variables

Install Django:
```bash
pip install django
```

## 🚀 Quick Start

# 1️⃣ Clone the repository
```bash
git clone https://github.com/HighsR/Password-Generator-DJANGO.git
cd Password-Generator-DJANGO
```
# 2️⃣ (Optional) Create and activate a virtual environment
```bash 
python -m venv .venv
```
Activate it:
- Windows: .venv\Scripts\activate

- macOS / Linux: source .venv/bin/activate
# 3️⃣ Install dependencies
```bash
pip install django
```
# 4️⃣ Set up the database
```bash
python manage.py migrate
```
# 5️⃣ Run the development server
```bash
python manage.py runserver
```
Now open: http://127.0.0.1:8000

## 🧭 Usage
1. Open the web app in your browser.

2. Select the length of your password (e.g., 8–20 characters).

3.Check which character types to include:

- ✅ Uppercase (A–Z)

- ✅ Lowercase (a–z)

- ✅ Numbers (0–9)

- ✅ Symbols (!, @, #, etc.)

4. Click Generate Password.

5. Your new password will appear instantly on screen.
  
6. Optionally, copy it using the browser’s clipboard function.

💡 Tip:
If you want to customize the design, edit the templates inside passgen/templates/ and adjust CSS to your liking.

## ⚖️ License / Attribution

This project was created for educational purposes using Django.
If parts of this code were developed as part of a tutorial or course (e.g., a Udemy Django course), please retain appropriate attribution and do not apply an open-source license unless permitted by the course author.

You may:

- Use or modify this project for personal and educational learning

- Share small snippets for demonstration or portfolio purposes

You may not:

- Redistribute, resell, or claim ownership of the original course materials

- Use this project commercially or upload full copies elsewhere

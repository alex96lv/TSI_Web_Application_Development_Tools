# Laboratory Work #2 - User Authentication System

Django web application with user registration, login, and authentication functionality.

## Features

- User Registration with email validation
- User Login/Logout system
- Protected home page (requires authentication)
- Password strength indicator
- CSS3 animations and responsive design
- JavaScript interactivity

## Technologies

- Python 3.x
- Django 5.2.9
- SQLite database
- Bootstrap 5
- Vanilla JavaScript

## Installation

1. Clone the repository
2. Create virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Start development server:
   ```bash
   python manage.py runserver
   ```

6. Open browser: `http://127.0.0.1:8000/`

## Project Structure

```
lab2_en/
├── manage.py
├── requirements.txt
├── login_system/        # Main project settings
├── accounts/            # Authentication app
├── templates/           # HTML templates
└── static/              # CSS and JavaScript
```

## Usage

1. Navigate to registration page: `/register/`
2. Create a new account
3. Login with your credentials: `/login/`
4. Access protected home page: `/`
5. Logout when done: `/logout/`

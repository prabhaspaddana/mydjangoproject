# auth_project
An authentication application built with Django, featuring user registration, login, password reset, and profile management.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction
This project is a basic user authentication system implemented using Django. It includes functionalities such as user registration, login, password change, password reset, and profile management. The project also includes a responsive UI with proper form validation and error handling.

## Features
- User Registration
- User Login
- Password Reset
- Profile Management
- Custom Password Validation
- Session Management
- Responsive UI

## Installation
Follow these steps to set up the project locally:

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/your_username/auth_project.git
   cd auth_project
   
2.Create and Activate a Virtual Environment:
sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3.Install Dependencies:
sh
pip install -r requirements.txt

4.Apply Migrations:
sh
python manage.py migrate

5.Create a Superuser:
sh
python manage.py createsuperuser

6.Run the Server:
sh
python manage.py runserver

Usage
Register a new user through the sign-up page.

Login with the registered credentials.

Access the profile management and password change features.

Reset the password if forgotten through the password reset feature.

Folder Structure
auth_project/
├── accounts/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── backends.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── change_password.html
│   │   ├── dashboard.html
│   │   ├── login.html
│   │   ├── profile.html
│   │   ├── signup.html
│   └── static/
│       ├── styles.css
│       └── scripts.js
├── auth_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── requirements.txt

Contributing
If you'd like to contribute to this project, please fork the repository and create a pull request with your changes.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
If you have any questions or suggestions, feel free to contact me at prabas.paddana@gmail.com.


### Instructions

1. Copy the entire content above, including the sections and formatting.
2. Create a new file named `README.md` in your project directory.
3. Paste the copied content into the `README.md` file.
4. Save the file and push the changes to your GitHub repository.

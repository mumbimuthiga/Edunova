# EduNova

EduNova is a Django-based educational platform for mapping a program to a job and the relevant skills required by a student , managing programs, courses, skills, and careers. It features a custom user model with email authentication, an admin dashboard, user signup with autogenerated passwords, and a modern Bootstrap-styled UI.

## Features

- Custom user model with email as the login field
- User signup with autogenerated password sent to email
- Email-based authentication (no username)
- Admin dashboard with statistics cards (courses, careers, skills)
- Course cards showing related skills and jobs
- Profile management for users
- Responsive Bootstrap 5 UI with icons

## Setup Instructions

1. **Clone the repository**
    ```bash
    git clone https://github.com/mumbimuthiga/edunova.git
    cd edunova
    ```

2. **Create and activate a virtual environment**
    ```bash
    python -m venv venv
    venv\Scripts\activate  # On Windows
    # or
    source venv/bin/activate  # On macOS/Linux
    ```

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure environment variables**
    - Copy `.env.example` to `.env` and set your secret key, database, and email settings.

5. **Apply migrations**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Create a superuser**
    ```bash
    python manage.py createsuperuser
    ```

7. **Run the development server**
    ```bash
    python manage.py runserver
    ```

8. **Access the app**
    - Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Project Structure

```
edunova/
├── adminsection/
│   └── templates/admin/
│       ├── dashboard.html
│       ├── profile.html
│       └── adminsection_base.html
├── users/
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   └── templates/users/
│       └── signup.html
├── programs/
│   └── models.py
├── pages/
│   └── templates/pages/
│       └── home.html
├── edunova/
│   └── settings.py
└── requirements.txt
```



This project is licensed under the MIT License.

---

**Made with Django & Bootstrap 5**

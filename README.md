# Django Blog Application

A simple and functional blog application built with Django, leveraging Class-Based Views (CBV) for the backend. The frontend is designed with Bootstrap, HTML, and JavaScript, ensuring a responsive and dynamic user experience. This project covers key Django concepts, including CRUD operations, user authentication, and templating.

## Features

- **Class-Based Views (CBV)**: The backend utilizes Django’s Class-Based Views, providing a clean and scalable approach for managing views and routes.
- **CRUD Functionality**: Users can easily create, read, update, and delete blog posts.
- **User Authentication**: The app includes user registration, login, and account management features.
- **Responsive Design**: The frontend is styled with Bootstrap, ensuring a mobile-friendly, responsive layout.
- **Dynamic User Interface**: JavaScript adds interactivity and dynamic elements to the frontend.

## Technologies Used

- **Backend**: Django (Python)
- **Frontend**: Bootstrap CSS, HTML, JavaScript
- **Database**: SQLite (default, configurable to PostgreSQL or MySQL)

## Setup & Installation

### Prerequisites

Ensure that you have the following installed:

- Python 3.x
- pip (Python package manager)

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/PhantomX95/django-simple-blog.git
   cd django-blog
   ```

2. Create a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the database migrations:

   ```bash
   python manage.py migrate
   ```

5. Create a superuser to access the Django admin panel:

   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

7. Open your browser and visit the application:

   [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Usage

- Access the blog on the homepage and view all posts.
- Users can register, log in, and manage their profiles.
- Admin users can manage blog posts through the Django admin interface.

## Contributing

Feel free to fork the repository and submit pull requests for bug fixes, new features, or enhancements!

---

This README provides a comprehensive guide to set up the Django Blog application, explains the core features and technologies, and offers instructions on how to contribute.

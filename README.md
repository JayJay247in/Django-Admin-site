# Django Admin Site Project

This project is a demonstration of a Django-based web application with a customized admin interface. It showcases how to use Django's powerful built-in admin features while tailoring them to specific project needs.

## Table of Contents

1.  [Introduction](#introduction)
2.  [Features](#features)
3.  [Getting Started](#getting-started)
    *   [Prerequisites](#prerequisites)
    *   [Installation](#installation)
    *   [Running the Development Server](#running-the-development-server)
    *   [Creating a Superuser](#creating-a-superuser)
4.  [Customization](#customization)
    *   [Admin Interface Customizations](#admin-interface-customizations)
    *   [Models and Fields](#models-and-fields)
5.  [Usage](#usage)
    *   [Accessing the Admin Site](#accessing-the-admin-site)
    *   [Using the Admin Panel](#using-the-admin-panel)
6.  [Contributing](#contributing)
7.  [License](#license)

## Introduction

This project is a learning resource designed to demonstrate how to build a Django application with a functional and customized admin interface. It explores key Django concepts such as models, views, templates, and the admin framework.

## Features

*   **Customized Django Admin:** The admin interface is tailored for the project's specific needs.
*   **Models and Data Management:** Defines Django models to represent application data (e.g., courses, instructors, students).
*   **Data Relationships:** Demonstrates relationships between different database models.
*   **User Authentication:** Integrated user authentication via Django's built-in system.
*   **Basic Django Functionality:** Implements core Django concepts like views, templates, urls, and settings.

## Getting Started

This section will guide you on setting up the project locally.

### Prerequisites

Before you begin, ensure that you have the following installed:

*   **Python 3.8 or higher:** You can download it from [https://www.python.org/downloads/](https://www.python.org/downloads/).
*   **pip (Python Package Installer):** Usually included with Python.
*   **PostgreSQL Database:** You can download it from [https://www.postgresql.org/download/](https://www.postgresql.org/download/) and will need a running database server.
*   **Git:** You can download it from [https://git-scm.com/downloads](https://git-scm.com/downloads) to clone this repository.

### Installation

1.  **Clone the Repository:**
    ```bash
    git clone <repository_url>
    cd <project_directory>
    ```
2.  **Create a Virtual Environment:**
    ```bash
    python3 -m venv djangoenv
    source djangoenv/bin/activate # On Linux or macOS
    djangoenv\Scripts\activate # On Windows
    ```
3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Configure Database:**
    *   Ensure that you have a PostgreSQL database created.
    *   Modify the `DATABASES` setting in `lab2_template/lab2_template/settings.py` to match your database credentials.
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'your_database_name',
            'USER': 'your_username',
            'PASSWORD': 'your_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

### Running the Development Server

1.  **Apply Migrations:**
    ```bash
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```
2.  **Start the Development Server:**
    ```bash
    python3 manage.py runserver
    ```
    This will start the Django development server and allow you to access the application at `http://127.0.0.1:8000/`.

### Creating a Superuser

To access the admin interface, you need to create a superuser account:

```bash
python3 manage.py createsuperuser
```bash

Follow the prompts to create a username, email address, and password.

Customization
Admin Interface Customizations
The admin site is customized in several ways, including:

Admin classes: Each model has a corresponding Admin class (adminsite/admin.py) to manage what fields are displayed in the admin interface, and allow access to specific models for specific user types.

Filters and Search: List filters and search functionality to easily find records in the admin interface.

Custom Actions: Added custom actions for tasks such as approving or rejecting submitted content.

Models and Fields
The project defines several Django models within the adminsite/models.py file. These include:

Course: Information about courses offered.

Instructor: Details about instructors.

Learner: Information about students taking the courses.

Lesson: The different lessons of the course.

Question: The different questions for each lesson.

Choice: The different choices for each question.

Enrollment: Information about which student is enrolled in each course.

Submission: Information about each student answer.

Each model has several fields with different data types (CharField, IntegerField, ForeignKey, etc.). The relationships between models are defined using ForeignKey, which means that models can relate to each other.

Usage
Accessing the Admin Site
Open your web browser.

Go to http://127.0.0.1:8000/admin.

Enter the username and password of the superuser you created earlier.

Using the Admin Panel
Once logged in, you'll see the customized admin panel, where you can:

Create new records.

View existing records.

Edit existing records.

Delete records.

Use search and filters.

Perform custom actions.

Contributing
Contributions are welcome! If you'd like to contribute to this project:

Fork the repository.

Create a new branch for your feature or bug fix.

Make your changes.

Submit a pull request.

License
This project is licensed under the MIT License


# Smart Task Management System

A multi-user task management web application built with Django.
Each user can securely manage their own personal tasks with authentication, filtering, pagination, and dashboard analytics.

## Project Objective

Build a secure multi-user task management system where:

* Users can register and login
* Users manage only their own tasks
* Dashboard shows task statistics
* Tasks can be filtered, searched, and exported
* System follows proper security practices


## Tech Stack

* Python 3.13
* Django 5.2
* SQLite
* Bootstrap 5
* HTML / CSS



##  Features

### Authentication

* User registration
* Login / Logout
* Profile auto-created using signals

###  Profile Model

python
user = OneToOneField(User)
profile_picture = ImageField
bio = TextField


Automatically created when a new user registers.

###  Task Model


python
title = CharField
description = TextField
status = Choices (Pending, In Progress, Completed)
priority = Choices (Low, Medium, High)
due_date = DateField
created_at = auto_now_add
updated_at = auto_now
owner = ForeignKey(User)

## Dashboard

After login, users can see:

* Total tasks
* Completed tasks
* Pending tasks
* Overdue tasks

Uses Django ORM filtering.


## Task Management (CRUD)

Users can:

* Create tasks
* Update tasks
* Delete tasks
* Mark tasks as completed

A user can never access another user's task.

All queries are filtered using:

python
Task.objects.filter(owner=request.user)


And secure object access:

python
get_object_or_404(Task, pk=pk, owner=request.user)


## Advanced Features Implemented

* Dark mode toggle
* Export tasks to CSV



## Installation Guide

### Clone Repository

bash
git clone https://github.com/yourusername/smart-task-manager.git
cd smart-task-manager


### Create Virtual Environment

bash
python -m venv venv
venv\Scripts\activate   # Windows


### Install Requirements

bash
pip install -r requirements.txt


### Run Migrations

bash
python manage.py migrate


### Create Superuser

bash
python manage.py createsuperuser


### Run Server

bash
python manage.py runserver

Open:


http://127.0.0.1:8000/



## Project Structure

smart_task_manager/
│
├── core/                # Project settings
├── tasks/               # Main app
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── signals.py
│   └── templates/
│
├── templates/
├── static/
├── media/
├── manage.py
└── requirements.txt


## Learning Outcomes

* Django project structure
* Authentication system
* Model relationships (OneToOne, ForeignKey)
* ORM filtering
* Pagination
* Secure multi-user architecture
* Bootstrap integration





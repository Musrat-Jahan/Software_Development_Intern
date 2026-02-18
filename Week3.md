## Week 3
## Task 1: Finding Error from Metro Blue website

Staff Account Issues
🐞 Bug 1: Profile Page Sidebar Does Not Scroll

Account Type: Staff

Page: Profile Page

Steps to Reproduce:

Login with a staff account

Navigate to Profile Page

Click Update Profile

Expected Result: ✅ Sidebar should automatically scroll to the top.

Actual Result: ❌ Sidebar does not scroll to the top.

🐞 Bug 2: No Option to Change Profile Picture

Account Type: Staff

Page: Profile Page

Description: No option available to change or update profile picture.

Expected Result: ✅ Staff users should be able to upload or change their profile picture.

Actual Result: ❌ No profile picture change option is visible.

🐞 Bug 3: Intern Edit Option Not Working Properly

Account Type: Staff/Admin

Page: Intern Management

Issues Observed:

Cannot select a user

Cannot edit name

Cannot edit email address

Expected Result: ✅ Admin/Staff should be able to select an intern and edit name and email.

Actual Result: ❌ Edit functionality is restricted or non-functional.

🐞 Bug 4: Enrollment Default Student Name Incorrect

Page: Enrollment (Add/Edit User)

Description: Default name appears as “Metroblue Admin” when adding or editing a student.

Expected Result: ✅ Field should be empty or reflect selected student.

Actual Result: ❌ Default value is incorrectly set to “Metroblue Admin”.

🐞 Bug 5: Course Page Currency Not Displayed

Page: Course Page

Description: Currency name or symbol is missing for course prices.

Expected Result: ✅ Display currency (e.g., $, AUD).

Actual Result: ❌ Currency information is missing.

🐞 Bug 6: Training Tracking – View Sessions Not Working

Module: Training Tracking

Steps to Reproduce:

Go to Training Tracking page

Click Action → View Sessions

Expected Result: ✅ Session details should display.

Actual Result: ❌ No content is shown.

🐞 Bug 7: Client Page Description in Different Language

Page: Client Page

Description: Client descriptions appear in a language other than English.

Expected Result: ✅ Content should display in English.

Actual Result: ❌ Content appears in an unknown language.

🔐 Admin Account Issues
🐞 Bug 8: Review Page Redirects to Another Dashboard

Account Type: Admin

Page: Review Section

Description: Clicking review redirects to a different dashboard.

Expected Result: ✅ Admin should review/edit in the same page/module.

Actual Result: ❌ Redirected to another dashboard.

🐞 Bug 9: Admin Menu Options Disappear After Clicking Edit

Account Type: Admin

Page: Admin Dashboard

Expected Menu:

Dashboard

Users

Accounts

Clients

Services

Training

Actual Result: ❌ Only limited options visible (Dashboard, Intern Tracking).

🐞 Bug 10: Admin Login Does Not Require Authentication

Account Type: Admin

Page: Login

Steps to Reproduce:

Navigate to login page

Select admin account

Expected Result: ✅ Prompt for authentication (username/password or MFA).

Actual Result: ❌ Admin logs in automatically.

Severity: 🔴 Critical (Security Issue)

👩‍💼 Staff Operation Account Issue
🐞 Bug 11: Staff Operations Button Missing

Account Type: Staff

Page: Staff Dashboard

Steps to Reproduce:

Login with staff account

Navigate to dashboard

Expected Result: ✅ Staff Operations button should be visible.

Actual Result: ❌ No button displayed.

🎓 Student Account Issue
🐞 Bug 12: Student Login Not Working

Account Type: Student

Page: Login

Steps to Reproduce:

Go to Metroblue login page

Enter valid student credentials

Click Login

Expected Result: ✅ Student should log in and access dashboard.

Actual Result: ❌ Login fails:

Student should be logged in successfully and redirected to the student dashboard.

Actual Result

Login fails with message:

"These credentials do not match."


---
## Django Installation

1. Create a folder in pc . like djangoproject

2. open that fo;der in vs code
3. Open Terminal
4. Command:

Create virtual environment
-> python -m venv venv

Activate virtual environment
 -> venv\Scripts\Activate

Upgrade pip
-> python -m pip install --upgrade pip

Install Django
-> pip install django

Create new Django project in current directory
-> django-admin startproject myproject .

Create a new Django app
-> python manage.py startapp myapp

Edit settings.py to add 'myapp' to INSTALLED_APPS (manual step)
Apply database migrations
-> python manage.py migrate

Create admin (superuser) account
-> python manage.py createsuperuser

Run the development server
-> python manage.py runserver

Deactivate virtual environment
-> deactivate

Save dependencies
-> pip freeze > requirements.txt

## Screenshots
* First Project in Django:

![First Django Project](https://github.com/Musrat-Jahan/Software_Development_Intern/raw/main/Images/DjangoProject1.png)

*Project Administration Site:
![First Django Project](https://github.com/Musrat-Jahan/Software_Development_Intern/blob/main/Images/PythonDjango%20Project%20SS.png)

* Second Project in Django:

![Second Project](https://github.com/Musrat-Jahan/Software_Development_Intern/raw/main/Images/MusratHomepageSS.png)


---

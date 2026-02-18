## Week 4
## Task:

This project is about building a simple multi-page information website for a company. 
This project using:
HTML
CSS
Bootstrap
JavaScript (Optional)

This is a frontend-only project. No Django is required for this assignment.
Project Requirements
website must contain the following pages:
- Home Page
- About Page
- Services Page
- Contact Page
- login page
- register page
  
 First, we need to create a folder in Django program called 
  
For Windows: Command in VS code terminal
venv\Scripts\activate

# Delete the old SQLite database
Remove-Item db.sqlite3

# Delete migrations folders
Remove-Item -Recurse -Force accounts\migrations
Remove-Item -Recurse -Force core\migrations

python manage.py makemigrations accounts
python manage.py migrate
python manage.py createsuperuser

for run:

venv\Scripts\activate
python manage.py runserver


Home page:

![images](https://github.com/Musrat-Jahan/Software_Development_Intern/blob/main/Images/Webpage%20home.png )\

Login Webpage:

![images](https://github.com/Musrat-Jahan/Software_Development_Intern/blob/main/Images/Login%20Webpage.png )

Register Webpage:

![images](https://github.com/Musrat-Jahan/Software_Development_Intern/blob/main/Images/Register%20Webpage.png)

Wrong Username/ Wrong password:

![images](https://github.com/Musrat-Jahan/Software_Development_Intern/blob/main/Images/Alert%20wrong%20credential.png )

Exist Email:

![images](https://github.com/Musrat-Jahan/Software_Development_Intern/blob/main/Images/Wrong%20Email.png )

Wrong Password: 

![images](https://github.com/Musrat-Jahan/Software_Development_Intern/blob/main/Images/Wrong%20pass.png)

Admin Site:

![images](https://github.com/Musrat-Jahan/Software_Development_Intern/blob/main/Images/PythonDjango%20Project%20SS.png)
User:
![images](https://github.com/Musrat-Jahan/Software_Development_Intern/blob/main/Images/Admin

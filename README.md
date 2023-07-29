# Udemy-Courses-Final-Project-Group1
1) virtual environment and necessary dependencies(optional)
   pip install virtualenv
3) create data tables using backup.sql file
4) make sure Django models managed flags are set to false
5) run python manage.py make migrations
6) run python manage.py migrate
7) run python manage.py runserver
Now you can go ahead and search but won't be able to update or delete. In order to do so change the managed flags in models to true
8) run python manage.py make migrations
9) run python manage.py migrate
10) run python manage.py runserver
Now your model is ready to edit, delete, or update
Make sure database name in settings.py matches database name of the tables

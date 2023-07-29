# Udemy-Courses-Final-Project-Group1
1) Virtual environment and necessary dependencies(optional)
   pip install virtualenv
3) Create data tables using backup.sql file
4) Make sure Django models managed flags are set to false
5) Run python manage.py make migrations
6) Run python manage.py migrate
7) Run python manage.py runserver
(Now you can go ahead and search but won't be able to update or delete. In order to do so change the managed flags in models to true.)
8) Run python manage.py make migrations
9) Run python manage.py migrate
10) Run python manage.py runserver
(Now your model is ready to edit, delete, or update.
Make sure database name in settings.py matches database name of the tables)
Note: If you did not have tables in the database you could run it without the model flags and add the data later. We had to set our flags since we had created the database first.

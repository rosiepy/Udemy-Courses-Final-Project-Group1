# SET THE NAMESPACE!
from . import views
from django.urls import path
app_name = 'courses'

# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
    path('add-course/', views.create, name='add-course'),
    path('delete_course/<int:course_id>/', views.delete, name='delete_course'),
    path('update_course/<int:course_id>/', views.update, name='update_course'),
]

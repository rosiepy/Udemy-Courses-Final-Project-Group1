from django import forms
from django.contrib.auth.models import User
from courses.models import UserProfileInfo, Udemy

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('telephone',)
class MainCoursesForm(forms.ModelForm):

    class Meta:

        model = Udemy
        fields = [
            "course_id",
            "course_title",
            "url",
            "is_paid",
            "price",
            "num_subscribers",
            "num_reviews",
            "num_lectures",
            "level",
            "content_duration",
            "published_timestamp",
            "subject"
        ]

from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):

    # Create relationship
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=15)


    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username


class Level(models.Model):
    level_id = models.AutoField(primary_key=True)
    level = models.CharField(max_length=255, null=True)

    class Meta:
        managed = True
        db_table = 'level'
    def __str__(self):
        return f"{self.level }"


class Subjects(models.Model):
    subject_id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=255, null=True)
    class Meta:
        managed = True
        db_table = 'subjects'
    def __str__(self):
        return f"{self.subject }"

class Price(models.Model):
    price_id = models.AutoField(primary_key=True)
    price = models.DecimalField(max_digits=10, decimal_places = 2)

    class Meta:
        managed = True
        db_table = 'price'
    def __str__ (self):
        return f"Price {self.price}  (ID :{self.id})"

class Udemy(models.Model):
    course_id = models.IntegerField(primary_key=True)
    course_title = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    is_paid = models.BooleanField()
    num_subscribers = models.IntegerField()
    num_reviews = models.IntegerField()
    num_lectures = models.IntegerField()
    content_duration = models.DecimalField(max_digits=10, decimal_places=3)
    published_timestamp = models.DateTimeField()
    level = models.ForeignKey(Level, default=None, on_delete=models.SET_DEFAULT)
    subject = models.ForeignKey(Subjects, default=None, on_delete=models.SET_DEFAULT)
    price = models.ForeignKey(Price, on_delete=models.SET_NULL,null=True)

    class Meta:
        managed = True
        db_table = 'courses'
    def __str__(self):
        return f"Udemy courses{self.course_title } (ID: {self.course_id})"

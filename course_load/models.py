from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Department(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Faculty(models.Model):
    psrn = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length = 100)
    department = models.ForeignKey(Department, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Course(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length = 100)
    l_number = models.IntegerField()
    t_number = models.IntegerField()
    p_number = models.IntegerField()
    ic = models.ForeignKey(Faculty, default=None, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class CourseFaculty(models.Model):
    SECTION_TYPES = (
        ('L', 'Lecture'),
        ('T', 'Tutorial'),
        ('P', 'Practical'),
        ('I', 'Independent'),
    )
    section_type = models.CharField(max_length=1, choices=SECTION_TYPES)
    course = models.ForeignKey(Course, default=None, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Faculty, default=None, on_delete=models.CASCADE)

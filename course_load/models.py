from django.db import models

# Create your models here.

class Department(models.Model):
    code = models.models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Faculty(models.Model):
    psrn = models.models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length = 100)
    department = models.ForeignKey(Department, default=None, on_delete=models.CASCADE, on_update=models.CASCADE)

    def __str__(self):
        return self.name

class Course(models.Model):
    code = models.models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length = 100)
    l_number = models.models.IntegerField()
    t_number = models.models.IntegerField()
    p_number = models.models.IntegerField()
    ic = models.ForeignKey(Faculty, default=None, on_delete=models.CASCADE, on_update=models.CASCADE)
    department = models.ForeignKey(Department, default=None, on_delete=models.CASCADE, on_update=models.CASCADE)

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
    course = models.ForeignKey(Course, default=None, on_delete=models.CASCADE, on_update=models.CASCADE)
    instructor = models.ForeignKey(Faculty, default=None, on_delete=models.CASCADE, on_update=models.CASCADE)

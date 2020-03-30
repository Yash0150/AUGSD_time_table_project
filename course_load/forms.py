from django import forms
from .models import Department, Course, Instructor

class CommentFileForm(forms.ModelForm):
    class Meta:  
        model = Department  
        fields = ['comment_file']
        labels = {
            "comment_file": "Comment file",
        }

class AddCourseForm(forms.ModelForm):
    class Meta:  
        model = Course  
        fields = ['code', 'name', 'department', 'course_type']
        labels = {
            'code': 'Course code',
            'code': 'Course name'
        }

class AddInstructorForm(forms.ModelForm):
    class Meta:  
        model = Instructor  
        fields = ['psrn_or_id', 'name', 'department', 'instructor_type']
        labels = {
            'psrn_or_id': 'PSRN/ID'
        }

class UpdateCourseForm(forms.ModelForm):
    class Meta:  
        model = Course  
        fields = ['code', 'name', 'department', 'course_type']
        labels = {
            'code': 'Course code',
            'code': 'Course name'
        }

class UpdateInstructorForm(forms.ModelForm):
    class Meta:  
        model = Instructor  
        fields = ['psrn_or_id', 'name', 'department', 'instructor_type']
        labels = {
            'psrn_or_id': 'PSRN/ID'
        }
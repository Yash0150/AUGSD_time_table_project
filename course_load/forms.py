from django import forms
from .models import Department

class CommentFileForm(forms.ModelForm):
    class Meta:  
        model = Department  
        fields = ['comment_file']
        labels = {
            "comment_file": "Comment file",
        }
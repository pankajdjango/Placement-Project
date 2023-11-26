# placement_app/forms.py
from django import forms
from .models import Companies, Interviews, Placements, Students

class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['name', 'email', 'branch', 'gpa']

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['maxlength'] = 50
            

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Companies
        fields = ['co_name', 'industry', 'location']
    
    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['maxlength'] = 50

from django import forms
from  .import models

class StudnetForm(forms.ModelForm):
    class Meta:
        model = models.StudentModel
        fields = '__all__'
        labels = {
            'name': 'Student Name',
            'roll' : 'Student Roll',
        }
        widgets = {
            'name': forms.TextInput(attrs = { 'placeholder': 'Type your name',}),
            'roll': forms.TextInput(attrs = { 'placeholder': 'Type your roll no',}),
            'father_name': forms.TextInput(attrs = { 'placeholder': 'Type your father name',}),
            'address': forms.TextInput(attrs = { 'placeholder': 'Type your address',}),
        }

        # help_texts = {
        #     'name' : 'Type your full name',
        # }

        error_messages = {
            'name' : {'required': 'your name is must requere to be unique'}
        }

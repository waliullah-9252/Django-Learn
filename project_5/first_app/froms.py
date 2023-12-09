from django import forms

from django.core import validators

class contactForm(forms.Form):
    name = forms.CharField(label = 'User Name', required=False, help_text='Total length must be 70 characters', widget = forms.Textarea(attrs = {'placeholder' : 'Enter your name'}))
    email = forms.EmailField(label = 'User Email')
    age = forms.IntegerField()
    weight = forms.FloatField()
    balance = forms.DecimalField()
    date = forms.DateField(widget= forms.DateInput(attrs = {'type': 'date'}))
    Appoinment = forms.DateTimeField(widget= forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    CHOICES = [('S','Small'), ('M', 'Medium'), ('L', 'Large')]
    Size = forms.ChoiceField(choices=CHOICES, widget= forms.RadioSelect())
    MEAL = [('Mashroom','Mashroom'), ('SoyaSouch','SoyaSouch'),('Beef','Beef')]
    Pizza = forms.MultipleChoiceField(choices=MEAL, widget=forms.CheckboxSelectMultiple())
    check = forms.BooleanField()

    # file_upload = forms.FileField()

# student forms with validation
# class StudentForm(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)
    # def clean_name(self):
    #     valname = self.cleaned_data['name']
    #     if len(valname) < 10:
    #         raise forms.ValidationError('Enter your name at least 10 characters')
    #     return valname
    # def clean_email(self):
    #     valemail = self.cleaned_data['email']
    #     if '.com' not in valemail:
    #         raise forms.ValidationError('Please enter a valid email address with .com')
    #     return valemail

    # def clean(self):
    #     cleaned_data = super().clean()
    #     valname = self.cleaned_data['name']
    #     valemail = self.cleaned_data['email']
    #     if len(valname) < 10:
    #         raise forms.ValidationError('Enter your name at least 10 characters')
    #     if '.com' not in valemail:
    #         raise forms.ValidationError('Please enter a valid email address with .com')
        
# use not built in funciton 
def value_check(value):
    if len(value) < 10:
        raise forms.ValidationError('Your text must be at least 10 characters')


# student forms with validation built in functions
class StudentForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput, validators=[validators.MinLengthValidator(10, message='Enter your name at least 10 characters'), validators.MaxLengthValidator(30, message='Enter your name at most 30 characters')])

    text = forms.CharField(widget=forms.Textarea, validators = [value_check])

    email = forms.CharField(widget=forms.EmailInput, validators=[validators.EmailValidator('Please enter a valid email address')])

    age = forms.IntegerField(validators=[validators.MinValueValidator(15, message='Age must be at least 15'), validators.MaxValueValidator(40, message='Age must be at most 40')])

    files = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf','jpg'], message='file must be .pdf')])

# password validation project 
class PasswordValidationProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    def clean(self):
        cleaned_data = super().clean()
        valname = cleaned_data['name']
        val_pass = cleaned_data['password']
        val_con_pass = cleaned_data['confirm_password']
        if len(valname) < 10:
            raise forms.ValidationError('Enter your name at least 10 characters')
        if val_pass != val_con_pass:
            raise forms.ValidationError('Passwords do not match! Please enter passwod and confirm password same as entered')
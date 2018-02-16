from django import forms

class TravellerForm(forms.Form):
    email = forms.CharField(label='Email', max_length=100)
    firstname = forms.CharField(label='First Name', max_length=50)
    lasname = forms.CharField(label='Last Name', max_length=50)
    password = forms.CharField(label='Password', max_length=50)
    icode = forms.CharField(label='Detination country', max_length=20)
    sdate = forms.DateTimeField(label='Start Date')
    edate = forms.DateTimeField(label='End Date')
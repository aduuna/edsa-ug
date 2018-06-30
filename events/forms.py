from django import forms

class EventRegisterForm(forms.Form):
	name = forms.CharField(max_length=120,widget=forms.TextInput(attrs={'class':'form-control'}))
	email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
	
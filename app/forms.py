from django import forms

class TodoForm(forms.Form):
  title = forms.CharField(max_length=100, label='タイトル')
  deadline = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='期限')
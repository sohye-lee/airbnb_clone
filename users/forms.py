from django import forms
from . import models

class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(username=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                # Not general error, but an error identified which field this error comes from
                self.add_error("password", forms.ValidationError("Password does not match."))
        except models.User.DoesNotExist:
            raise forms.ValidationError("username", "User does not exist.")
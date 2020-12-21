from django import forms
from django.contrib.auth.models import User
from .models import Post, TreeComment


class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
	password = forms.CharField(label='Password',
							   widget=forms.PasswordInput)
	password2 = forms.CharField(label='Repeat password',
							 	widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ('username', 'first_name', 'email')

	def clean_password2(self):
		cd = self.cleaned_data
		if cd['password'] != cd['password2']:
			raise forms.ValidationError('Passwords don\'t match.')
			
		return cd['password2']


class CommentForm(forms.ModelForm):
	class Meta:
		model = TreeComment
		# We'll fill other fields automatically by
		# data from logged in user
		fields = ('body',)


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'slug', 'body')
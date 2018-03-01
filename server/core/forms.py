# -*- coding: utf-8 -*-

from django import forms

from user.models import Profile


class SignupForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone', )

    def signup(self, request, user):
        user.save()

        profile = Profile()
        profile.user = user
        profile.phone = self.cleaned_data['phone']
        profile.save()

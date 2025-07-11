from django import forms
from django.contrib.auth.models import User
from core.models import UserProfile, ConfiguracionEscolar


class UserProfileForm(forms.ModelForm):

    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(required=False)
    avatar = forms.ImageField(required=False)

    class Meta:
        model = UserProfile
        fields = ['avatar']

    def __init__(self, *args, **kwargs):
        user = kwargs.get('user')
        super(UserProfileForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['first_name'].initial = user.first_name
            self.fields['last_name'].initial = user.last_name
            self.fields['email'].initial = user.email

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()

        # Actualizamos los campos del User model
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.save()

        # Guardamos los cambios en UserProfile (si es necesario)
        user_profile = super().save(commit=False)
        if commit:
            user_profile.save()

        return user_profile

    # Validación para el avatar (opcional)
    def clean_avatar(self):
        avatar = self.cleaned_data.get('avatar')
        if avatar and avatar.size > 5 * 1024 * 1024:  # Limitar el tamaño de la imagen a 5MB
            raise forms.ValidationError("El archivo es demasiado grande. El tamaño máximo permitido es 5MB.")
        return avatar
    
class ConfiguracionEscolarForm(forms.ModelForm):
    class Meta:
        model = ConfiguracionEscolar
        fields = '__all__'
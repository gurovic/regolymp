from django.contrib.auth.forms import UserCreationForm
from .models import Organizer
from django.core.exceptions import ValidationError 

class OrganizerCreateForm(UserCreationForm):
    class Meta:
        model = Organizer
        fields = ['first_name', 'second_name', 'last_name', 
                  'email', 'mobile', 'contacts', 'username']

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            Organizer.objects.get(username=username)
        except Organizer.DoesNotExist:
            return username
        raise ValidationError(self.error_messages['duplicate_username'])

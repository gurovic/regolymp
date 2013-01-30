from .models import Organizer
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from .forms import OrganizerCreateForm
from django.contrib.auth.models import UserManager
from django.utils import timezone


def create_user(request):
    is_success = False
    if request.method == 'POST':
        form = OrganizerCreateForm(request.POST)
        if form.is_valid():
                print(form.cleaned_data)
                login = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                email = form.cleaned_data['email']
                
                createuser(login, email, password, 
                                 first_name = form.cleaned_data['first_name'],
                                 second_name = form.cleaned_data['second_name'],
                                 last_name = form.cleaned_data['last_name'],
                                 place = form.cleaned_data['place'],
                                 contacts = form.cleaned_data['contacts'],
                                 mobile = form.cleaned_data['mobile'],
                                )
                is_success = True
    else:
        form = OrganizerCreateForm()
    return render_to_response('register.html', {
        'form': form,
        'is_success': is_success,
    }, RequestContext(request))

def createuser(username, email=None, password=None, **extra_fields):
        now = timezone.now()
        if not username:
            raise ValueError('The given username must be set')
        email = UserManager.normalize_email(email)
        user = Organizer(username=username, email=email,
                          is_staff=False, is_active=True, is_superuser=False,
                          last_login=now, date_joined=now, **extra_fields)

        user.set_password(password)
        user.save()
        return user

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from forms import UserProfileCreationForm

@login_required
def account(request):
    return render(request, 'core/profile.html')

def register(request):
    if request.method == 'POST':
        form = UserProfileCreationForm(request.POST)
        if form.is_valid():
            #Save user and authenticate
            form.save()

            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            #Save profile data
            profile = user.get_profile()
            profile.zip = form.cleaned_data['zip']
            profile.save()
            #Log the user in
            login(request, user)
            return redirect('register_done')
    else:
        form = UserProfileCreationForm()
    return render(request, "registration/register.html", {'form': form})

def register_done(request):
    return render(request, "registration/register_done.html")
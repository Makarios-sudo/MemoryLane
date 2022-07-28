from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from users.models import Profile
from .forms import UpdateProfileForm, userRegistrationForm
from django.contrib.auth.decorators import login_required
# Create your views here.


# login user
def userLogin(request):
    page = "login"
    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password').lower()
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login was succesfull")
            return redirect("memoryGallery")
        else:
            messages.error(request, "Username or Password is Incorrect")
            return redirect("userLogin")
            
    context = {"page":page}   
    return render(request, "users/Login_register.html",context )
    

# register user
def userRegistration(request):
    form = userRegistrationForm()

    if request.method == "POST":
        form = userRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, "Registration was successfull")
            return redirect("userLogin")
        else:
            messages.error(request, "Registeration Failed, Please ensure the passwords are correct.")

    context = {'form': form}
    return render(request, 'users/Login_register.html', context )


#  logout user
def userLogout(request):
    logout(request)
    messages.success(request, "Logout was succesfull")
    return redirect("index")

# getting individual profile
@login_required(login_url='index')
def profile(request, ):
    page = "profile"
    profiles = Profile.objects.all()

    context = {"profiles":profiles, "page":page }
    return render(request, "users/profile.html", context)


# update profile
@login_required(login_url='index')
def updateProfile(request, pk):
    
    profile = Profile.objects.get(id=pk)
    form = UpdateProfileForm(instance=profile)

    if request.method == "POST":
        form = UpdateProfileForm(request.POST, request.FILES, instance=profile,)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Profile was succesfully Updated")
            return redirect("profile")

    context = {"form":form, "profile":profile}
    return render(request, "users/profile.html", context)


    

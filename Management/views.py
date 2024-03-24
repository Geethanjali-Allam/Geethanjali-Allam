from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django import forms
from django.urls import reverse
from .models import Employee, Complaint
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect

#Adding Favorite List
favorites = []

#Adding Complaint List
complaint_author = []
complaint_email = []
complaint_type = []
complaint_subject = []
complaint_message = []

class BaseUserForm(forms.Form):
    Email = forms.EmailField(label="Your Email:", max_length=64)
    Password = forms.CharField(label="Password", max_length=64)

class NewFavForm(forms.Form):
    new_favorite = forms.CharField(label="New Favorite", required="True")

class NewComplaintForm(forms.Form):
    name = forms.CharField(label="Your name:", max_length=100, required="True")
    sender = forms.EmailField(label="Your Email:", required="True")
    c_type = forms.CharField(label="Complaint Type:", required="True")
    subject = forms.CharField(label="Subject:", min_length=10, required="True")
    message = forms.CharField(label="Message:", max_length=300, required="True")

class NewSearchForm(forms.Form):
    query = forms.CharField(label="Employee Name:", max_length=100, required="True")

class NewSignupForm(forms.Form):
    Name = forms.CharField(label="Your Name:",max_length=64)
    Email = forms.EmailField(label="Your Email:",max_length=64)
    Password = forms.CharField(label="Password",max_length=64)
    Position = forms.CharField(label="Your Position",max_length=64)
    Salary = forms.IntegerField(label="Your Salary:")

class LoginForm(AuthenticationForm):
    Email = forms.EmailField(label="Your Email:", max_length=64)
    Password = forms.CharField(label="Password", max_length=64)
class UpdateComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['author', 'email', 'complaint_type', 'subject', 'message']
# Create your views here.
def index(request):
    return render(request, "Management/index.html", {
        "favorites": favorites
    })
@login_required
def view_fav(request):
    return render(request, "Management/favourite.html", {
        "favorites": favorites
    })
@login_required
def add_fav(request):
    if request.method == "POST":
        form = NewFavForm(request.POST)
        if form.is_valid():
            new_favorite = form.cleaned_data["new_favorite"]
            favorites.append(new_favorite)
            return HttpResponseRedirect(reverse("Management:Add_Favourite"))
        else:
            return render(request, "Management/add_favourite.html", {
                "form": form,
                "favorites": favorites
            })
    
    return render(request, "Management/add_favourite.html", {
        "form": NewFavForm(),
        "favorites": favorites
    })

def add_complaint(request):
    if request.method == "POST":
        form = NewComplaintForm(request.POST)
        if form.is_valid():
            # Save the complaint to the database
            complaint = Complaint(
                author=form.cleaned_data["name"],
                email=form.cleaned_data["sender"],
                complaint_type=form.cleaned_data["c_type"],
                subject=form.cleaned_data["subject"],
                message=form.cleaned_data["message"]
            )
            complaint.save()
            return HttpResponseRedirect(reverse("Management:View_Complaint"))
        else:
            error_message = "Invalid form submission. Please check your input."
            return render(request, "Management/add_complaint.html", {
                "form": form,
                "error_message": error_message,
                "favorites": favorites
            })

    return render(request, "Management/add_complaint.html", {
        "form": NewComplaintForm(),
        "favorites": favorites
    })

@login_required
def view_complaint(request):
    complaints = Complaint.objects.all()
    return render(request, "Management/complaint.html", {
        "Complaint": complaints,
        "favorites": favorites
    })
@login_required
def update_complaint(request, complaint_id):
    complaint = get_object_or_404(Complaint, id=complaint_id)
    if request.method == "POST":
        form = UpdateComplaintForm(request.POST, instance=complaint)
        if form.is_valid():
            form.save()
            return redirect("Management:View_Complaint")
    else:
        form = UpdateComplaintForm(instance=complaint)

    return render(request, "Management/update_complaint.html", {
        "form": form,
        "complaint_id": complaint_id,
        "favorites": favorites
    })

@login_required
def delete_complaint(request, complaint_id):
    complaint = get_object_or_404(Complaint, id=complaint_id)
    if request.method == "POST":
        complaint.delete()
        return redirect("Management:View_Complaint")

    return render(request, "Management/delete_complaint.html", {
        "complaint": complaint,
        "favorites": favorites
    })

@login_required
def search(request):
    result = "NONE"
    if request.method == "POST":
        form = NewSearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data["query"]
            result = Employee.objects.filter(Name__icontains=query)
            return render(request, "Management/search.html", {
                "form": form,
                "result": result,
                "method": request.method,
                "favorites": favorites
            })
        else:
            error_message = "Invalid form submission. Please check your input."
            return render(request, "Management/search.html", {
                "result": result,
                "form": form,
                "error_message": error_message,
                "method": request.method,
                "favorites": favorites
            })

    return render(request, "Management/search.html", {
        "result": result,
        "form": NewSearchForm(),
        "method": request.method,
        "favorites": favorites
    })

def sign_up(request):
    if request.method == "POST":
        form = NewSignupForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["Name"]
            email = form.cleaned_data["Email"]
            password = form.cleaned_data["Password"]
            position = form.cleaned_data["Position"]
            salary = form.cleaned_data["Salary"]
            new_employee = Employee(Name= name, Email= email, Password= password, Position= position, Salary= salary)
            new_employee.save()
            return HttpResponseRedirect(reverse("Management:Sign_Up"))
        else:
            return render(request, "Management/signup.html", {
                "form": form,
                "favorites": favorites
            })
    
    return render(request, "Management/signup.html", {
        "form": NewSignupForm(),
        "favorites": favorites
    })

def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')  # Assuming you're using username to authenticate
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("Management:Home")) 
            else:
                error_message = "Invalid login credentials. Please try again."
                return render(request, "Management/login.html", {"form": form, "error_message": error_message})
        else:
            error_message = "Invalid form submission. Please check your input."
            return render(request, "Management/login.html", {"form": form, "error_message": error_message})

    form = AuthenticationForm()  # Create a new instance of the form for GET requests
    return render(request, "Management/login.html", {"form": form})

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse("Management:login"))
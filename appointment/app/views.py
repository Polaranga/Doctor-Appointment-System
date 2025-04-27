from django.shortcuts import render
from Users.models import User
from django.db.models import Q

# Create your views here.
def home(request):
    return render(request,'home.html')
def signup(request):
    return render(request,'signup.html')
def login(request):
    return render(request,'login.html')
def aboutus(request):
    return render(request,'aboutus.html')
def contact(request):
    return render(request,'contact.html')
def insert_data(request):
    if request.method=='POST':
        Firstname=request.POST.get('Firstname')
        Lastname=request.POST.get('Lastname')
        Mobileno=request.POST.get('Mobileno')
        Email=request.POST.get('Email')
        Password=request.POST.get('Password')
        Location=request.POST.get('Location')
        Zipcode=request.POST.get('Zipcode')
        Gender=request.POST.get('Gender')
        Usertype=request.POST.get('Usertype')
        Cause=request.POST.get('Cause')
        Age=request.POST.get('Age')
        Age = int(Age) if Age and Age.isdigit() else 0
        Insurance=request.POST.get('Insurance')
        Specialization=request.POST.get('Specialization')
        Availability=request.POST.get('Availability')
        Experience=request.POST.get('Experience')
        Experience = int(Experience) if Experience and Experience.isdigit() else 0
        Created_at=request.POST.get('Created_at')
        userdata=User(Firstname=Firstname,Lastname=Lastname,Mobileno=Mobileno,
                   Email=Email,Password=Password, Location=Location, Zipcode=Zipcode,
                   Gender=Gender,Usertype=Usertype,Cause=Cause,Age=Age,
                   Insurance=Insurance,Specialization=Specialization,Availability=Availability,
                   Experience=Experience,Created_at=Created_at)
        userdata.save()
        return render(request,'login.html')
    else:
        return render(request,'signup.html')
        


def login_user(request):
    if request.method == 'POST':
        Email = request.POST.get('Email')
        Password = request.POST.get('Password')

        user = User.objects.filter(Email=Email, Password=Password).first()

        if user:
            return render(request, 'home.html', {'user': user})
        else:
            return render('signup.html')  # User doesn't exist, go to signup

    return render(request, 'login.html')

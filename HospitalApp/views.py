from django.shortcuts import render, redirect
from HospitalApp.models import Members, Contacts, Users


# Create your views here.
def index(request):
    if request.method == 'POST':
        messages = Contacts(name=request.POST['name'],
                            email=request.POST['email'],
                            subject=request.POST['subject'],
                            message=request.POST['message'])

        messages.save()
        return redirect('/')
    else:
        return render(request, 'index.html')


def inner(request):
    return render(request, 'inner-page.html')


def register(request):
    if request.method == 'POST':
        members = Members(username=request.POST['username'],
                          email=request.POST['email'],
                          password=request.POST['password'])

        members.save()
        return redirect('/login')
    else:
        return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')


def upload(request):
    return render(request, 'upload.html')


def details(request):
    messages = Contacts.objects.all()
    return render(request, 'details.html', {'details': details})


def user(request):
    myusers = Users.objects.all()
    return render(request, 'users.html', {'myusers': myusers})


def adminhome(request):
    if request.method == 'POST':
        if Members.objects.filter(username=request.POST['username'],
                                  password=request.POST['password']).exists():
            memeber = Members.objects.get(username=request.POST['username'],
                                          password=request.POST['password'])
            return render(request, 'adminhome.html', {'memeber': memeber})
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

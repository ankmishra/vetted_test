from django.shortcuts import render
from authen.forms import UserForm, UserProfileInfoForm, CompanyInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from authen.models import CompanyInfo, UserProfileInfo, AdminProfileInfo
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request,'authen/index.html')


@login_required
def special(request):
    return HttpResponse("You are logged in !")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'authen/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

def addCompany(request):
    added = False
    if request.method == 'POST':
        company_form = CompanyInfoForm(data=request.POST)
        if company_form.is_valid():
            company = company_form.save()
            company.save()
            added = True
        else:
            print(add_company.errors)
    else:
        company_form = CompanyInfoForm()
    return render(request,'authen/addcompany.html',
                          {'company_form':company_form,
                           'added':added})

def update(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST,instance=request.user)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'authen/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})


def addadmin(request):
    added = False
    if request.method == 'POST':
        com = request.POST.get('company')
        u = request.POST.get('user')
        user = User.objects.filter(username=u).first()
        company = CompanyInfo.objects.filter(name=com).first()
        admin = AdminProfileInfo()
        admin.employee = user
        admin.company = company
        user.is_staff=True
        user.save()
        admin.save()
        added = True
        # admin_form = AdminProfileInfo(data=request.POST)
        # if admin_form.is_valid():
        #     admin = admin_form.save()
        #     admin.save()
        #     added = True
        # else:
        print("admin_form.errors")
    companies = CompanyInfo.objects.all()
    users = User.objects.all()
    return render(request,'authen/addadmin.html',
                          {'companies':companies,
                          'users':users,
                           'added':added})



def removeCompany(request):
    remove = False
    if request.method == 'POST':
        company = request.POST.get('company')
        remove = True
        company = CompanyInfo.objects.filter(name=company).first()
        company.delete()
    companies = CompanyInfo.objects.all()
    return render(request,'authen/remove.html',
                          {'companies':companies,
                           'remove':remove})


def removeEmployee(request):
    remove = False
    if request.method == 'POST':
        employee = request.POST.get('employee')
        user = User.objects.filter(username=employee).first()
        employee = UserProfileInfo.objects.get(user=user)
        employee.delete()
        remove = True
    employees = UserProfileInfo.objects.all()
    return render(request,'authen/removeemployee.html',
                          {'employees':employees,
                           'remove':remove})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'authen/login.html', {})

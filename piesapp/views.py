from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Pie
from .forms import RegisterForm, PieForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def login_register(request):
    register_form = RegisterForm()

    if request.method == 'POST':
        if 'register' in request.POST:
            register_form = RegisterForm(request.POST)
            if register_form.is_valid():
                user = register_form.save()
                messages.success(request, 'Account created successfully!')
                login(request, user) 
                return redirect('dashboard')  

        elif 'login' in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, "Invalid username or password!")

    return render(request, 'login_register.html', {'register_form': register_form})


@login_required
def dashboard(request):
    user_pies = Pie.objects.filter(baker=request.user)

    return render(request, 'dashboard.html', {'user_pies': user_pies})

@login_required
def add_pie(request):
    if request.method == 'POST':
        form = PieForm(request.POST)
        if form.is_valid():
            pie = form.save(commit=False)
            pie.baker = request.user
            pie.save()
            messages.success(request, "Pie added successfully!")
            return redirect('dashboard')
    else:
        form = PieForm()
    return render(request, 'add_pie.html', {'form': form})

@login_required
def create_pie(request):
    if request.method == 'POST':
        form = PieForm(request.POST)
        if form.is_valid():
            pie = form.save(commit=False)  
            pie.baker = request.user 
            pie.save()
            return redirect('all_pies')
    else:
        form = PieForm()

    return render(request, 'create_pie.html', {'form': form})

@login_required
def view_pie(request, id):
    pie = Pie.objects.filter(id=id).first()
    if pie is None:
        return redirect('all_pies')
    
    return render(request, 'view_pie.html', {'pie': pie})

@login_required
def edit_pie(request, id):
    pie = Pie.objects.filter(id=id).first()
    if pie is None or pie.baker != request.user:
        return redirect('all_pies')

    if request.method == 'POST':
        form = PieForm(request.POST, instance=pie)
        if form.is_valid():
            form.save()
            return redirect('all_pies')  
    else:
        form = PieForm(instance=pie)

    return render(request, 'edit_pie.html', {'form': form})

@login_required
def delete_pie(request, id):
    pie = Pie.objects.filter(id=id).first()  
    if pie and pie.baker == request.user:  
        pie.delete()  
    return redirect('all_pies')  

@login_required
def all_pies(request):
    pies = Pie.objects.all()
    return render(request, 'all_pies.html', {'pies': pies})

def logout_view(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('login_register')

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import ShortURL
from .forms import Form



def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save()          
        login(request, user)        
        return redirect('dashboard')

    return render(request, 'register.html', {'form': form})


def login_view(request):   
    form = AuthenticationForm(data=request.POST or None)

    if form.is_valid():
        login(request, form.get_user())
        return redirect('dashboard')

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    urls = ShortURL.objects.filter(user=request.user).order_by('-created_at')
    form = Form(request.POST or None)

    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect('dashboard')

    return render(request, 'dashboard.html', {'urls': urls, 'form': form})


@login_required
def edit_url(request, pk):
    obj = get_object_or_404(ShortURL, pk=pk, user=request.user)

    form = Form(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect('dashboard')

    return render(request, 'edit.html', {'form': form, 'obj': obj})


@login_required
def delete_url(request, pk):
    obj = get_object_or_404(ShortURL, pk=pk, user=request.user)

    if request.method == 'POST':
        obj.delete()
        return redirect('dashboard')

    return render(request, 'confirm_delete.html', {'obj': obj})


def redirect_url(request, short_key):
    obj = get_object_or_404(ShortURL, short_key=short_key)
    obj.save()
    return redirect(obj.original_url)
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from .models import Feature, Todo, SuggestedFeature
from .forms import (
    CustomUserCreationForm, 
    CustomAuthenticationForm,
    TodoForm,
    SuggestedFeatureForm,
    FeatureForm
)


def todohome(request: HttpRequest) -> HttpResponse:
    """Render homepage with features showcase"""
    features = Feature.objects.filter(is_active=True).order_by('order')
    return render(request, "todowork.html", {'features': features})


def about(request: HttpRequest) -> HttpResponse:
    """Render about page"""
    return render(request, 'about.html')


def features_page(request: HttpRequest) -> HttpResponse:
    """
    Render features list with user authentication status.
    Shows active features and allow logged-in users to suggest new ones.
    """
    active_features = Feature.objects.filter(is_active=True).order_by('order')
    
    context = {
        'features': active_features,
        'suggested_features': None,
    }
    
    # Show suggested features to logged-in users
    if request.user.is_authenticated:
        context['suggested_features'] = SuggestedFeature.objects.filter(
            is_approved=True
        ).order_by('-votes')
    
    return render(request, 'features.html', context)


def signup_view(request: HttpRequest) -> HttpResponse:
    """Handle user registration/signup"""
    if request.user.is_authenticated:
        return redirect('todo')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log user in after registration
            login(request, user)
            messages.success(request, f"Welcome {user.first_name or user.username}! Your account has been created.")
            return redirect('todo')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'signup.html', {'form': form})


def login_view(request: HttpRequest) -> HttpResponse:
    """Handle user login"""
    if request.user.is_authenticated:
        return redirect('todo')
    
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {user.first_name or user.username}!")
                return redirect('todo')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = CustomAuthenticationForm()
    
    return render(request, 'login.html', {'form': form})


def logout_view(request: HttpRequest) -> HttpResponse:
    """Handle user logout"""
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('todo')


@login_required(login_url='login')
def todos_list(request: HttpRequest) -> HttpResponse:
    """Display user's todos"""
    todos = Todo.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'todos_list.html', {'todos': todos})


@login_required(login_url='login')
def create_todo(request: HttpRequest) -> HttpResponse:
    """Create a new todo"""
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            messages.success(request, "Task created successfully!")
            return redirect('todos_list')
    else:
        form = TodoForm()
    
    return render(request, 'create_todo.html', {'form': form})


@login_required(login_url='login')
def edit_todo(request: HttpRequest, todo_id: int) -> HttpResponse:
    """Edit an existing todo"""
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, "Task updated successfully!")
            return redirect('todos_list')
    else:
        form = TodoForm(instance=todo)
    
    return render(request, 'edit_todo.html', {'form': form, 'todo': todo})


@login_required(login_url='login')
def delete_todo(request: HttpRequest, todo_id: int) -> HttpResponse:
    """Delete a todo"""
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    
    if request.method == 'POST':
        todo.delete()
        messages.success(request, "Task deleted successfully!")
        return redirect('todos_list')
    
    return render(request, 'delete_todo.html', {'todo': todo})


@login_required(login_url='login')
def suggest_feature(request: HttpRequest) -> HttpResponse:
    """Allow users to suggest new features"""
    if request.method == 'POST':
        form = SuggestedFeatureForm(request.POST)
        if form.is_valid():
            feature = form.save(commit=False)
            feature.user = request.user
            feature.save()
            messages.success(request, "Thank you! Your feature suggestion has been received.")
            return redirect('features')
    else:
        form = SuggestedFeatureForm()
    
    return render(request, 'suggest_feature.html', {'form': form})


def feature_add_view(request: HttpRequest) -> HttpResponse:
    """Admin feature creation (kept for compatibility)"""
    if not request.user.is_staff:
        messages.error(request, "You don't have permission to add features.")
        return redirect('features')
    
    if request.method == 'POST':
        form = FeatureForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Feature added successfully!")
            return redirect('features')
    else:
        form = FeatureForm()
    
    return render(request, 'createfeatures.html', {'form': form})

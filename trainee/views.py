from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Trainee
from .forms import TraineeForm


class TraineeListView(ListView):
    model = Trainee
    template_name = 'trainee/trainee_list.html'
    context_object_name = 'trainees'
    login_url = 'login'

class TraineeCreateView(CreateView):
    model = Trainee
    form_class = TraineeForm
    template_name = 'trainee/form.html'
    success_url = reverse_lazy('trainee_list')

class TraineeUpdateView(UpdateView):
    model = Trainee
    form_class = TraineeForm
    template_name = 'trainee/form.html'
    success_url = reverse_lazy('trainee_list')

class TraineeDeleteView(DeleteView):
    model = Trainee
    template_name = 'trainee/delete.html'
    success_url = reverse_lazy('trainee_list')

# class RegisterView(CreateView):
#     def get(self, request):
#         form = UserCreationForm()
#         return render(request, 'registration/register.html', {'form': form})

#     def post(self, request):
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()  
#             login(request, user) 
#             return redirect('trainee_list') 
#         return render(request, 'registration/register.html', {'form': form})
    

def RegisterView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() 
            login(request, user) 
            return redirect('trainee_list')  
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


class LoginView(LoginView):
    template_name = 'registration/login.html'
    def get_success_url(self):
        return reverse_lazy('trainee_list')


class LogoutView(LogoutView):
    next_page = 'login'


# from django.shortcuts import render, redirect, get_object_or_404
# from .models import Trainee
# from .forms import TraineeForm

# def trainee_list(request):
#     trainees = Trainee.objects.all()
#     return render(request, 'trainee/trainee_list.html', {'trainees': trainees})

# def add_trainee(request):
#     if request.method == "POST":
#         form = TraineeForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('trainee_list')
#     else:
#         form = TraineeForm()
#     return render(request, 'trainee/form.html', {'form': form})

# def update_trainee(request, pk):
#     trainee = get_object_or_404(Trainee, pk=pk)
#     if request.method == "POST":
#         form = TraineeForm(request.POST, instance=trainee)
#         if form.is_valid():
#             form.save()
#             return redirect('trainee_list')
#     else:
#         form = TraineeForm(instance=trainee)
#     return render(request, 'trainee/form.html', {'form': form})

# def delete_trainee(request, pk):
#     trainee = get_object_or_404(Trainee, pk=pk)
#     if request.method == 'POST':
#         trainee.delete()
#         return redirect('trainee_list')
#     return render(request, 'trainee/delete.html', {'trainee': trainee})

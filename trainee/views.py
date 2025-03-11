from django.shortcuts import render, redirect, get_object_or_404
from .models import Trainee
from .forms import TraineeForm

def trainee_list(request):
    trainees = Trainee.objects.all()
    return render(request, 'trainee/trainee_list.html', {'trainees': trainees})

def add_trainee(request):
    if request.method == "POST":
        form = TraineeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trainee_list')
    else:
        form = TraineeForm()
    return render(request, 'trainee/form.html', {'form': form})

def update_trainee(request, pk):
    trainee = get_object_or_404(Trainee, pk=pk)
    if request.method == "POST":
        form = TraineeForm(request.POST, instance=trainee)
        if form.is_valid():
            form.save()
            return redirect('trainee_list')
    else:
        form = TraineeForm(instance=trainee)
    return render(request, 'trainee/form.html', {'form': form})

def delete_trainee(request, pk):
    trainee = get_object_or_404(Trainee, pk=pk)
    if request.method == 'POST':
        trainee.delete()
        return redirect('trainee_list')
    return render(request, 'trainee/delete.html', {'trainee': trainee})

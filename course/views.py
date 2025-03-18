from django.shortcuts import render, redirect, get_object_or_404
from .models import Course
from .forms import CourseForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CourseSerializer

@api_view(['GET', 'POST'])
def course_list_create_api(request):
    if request.method == 'GET':
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ✅ API: تحديث كورس أو حذفه (Function-Based View)
@api_view(['PUT', 'DELETE'])
def update_delete_course_api(request, pk):
    course = get_object_or_404(Course, pk=pk)

    if request.method == 'PUT':
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        course.delete()
        return Response({'message': 'Course deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
def course_list(request):
    courses = Course.objects.values("id", "name", "description", "duration")
    return render(request, 'course/course_list.html', {'courses': courses})

def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'course/form.html', {'form': form})

def update_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)
    return render(request, 'course/form.html', {'form': form})

def delete_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    return render(request, 'course/delete.html', {'course': course})

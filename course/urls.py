from django.urls import path
from .views import *

urlpatterns=[
    path('', course_list, name='course_list'),
    path('add/', add_course, name='add_course'),
    path('update/<int:pk>/', update_course, name='update_course'),
    path('delete/<int:pk>/', delete_course, name='delete_course'),

    path('api/courses/', course_list_create_api, name='api-course-list-create'),
    path('api/courses/<int:pk>/', update_delete_course_api, name='api-course-update-delete'),

]
from django.urls import path
from .views import *

urlpatterns = [
    path('', TraineeListView.as_view(), name='trainee_list'),
    path('add/', TraineeCreateView.as_view(), name='add_trainee'),
    path('<int:pk>/update/', TraineeUpdateView.as_view(), name='update_trainee'),
    path('<int:pk>/delete/', TraineeDeleteView.as_view(), name='delete_trainee'),

    # Authentication URLs
    path('register/', RegisterView, name='register'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

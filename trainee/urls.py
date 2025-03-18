from django.urls import path
from .views import *

urlpatterns = [
    path('', TraineeListView.as_view(), name='trainee_list'),
    path('add/', TraineeCreateView.as_view(), name='add_trainee'),
    path('<int:pk>/update/', TraineeUpdateView.as_view(), name='update_trainee'),
    path('<int:pk>/delete/', TraineeDeleteView.as_view(), name='delete_trainee'),

    # Authentication URLs
    path('register/', RegisterView, name='register'),
    path('login/', TraineeLoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', TraineeLogoutView.as_view(), name='logout'),

    path('api/trainees/', TraineeListCreateAPIView.as_view(), name='api-trainee-list-create'),
    path('api/trainees/<int:pk>/', TraineeUpdateDeleteAPIView.as_view(), name='api-trainee-update-delete'),

]

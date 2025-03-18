from django.urls import path
from .views import TraineeListView, TraineeDetailView, TraineeDeleteView,TraineeAddView,TraineeUpdateView
from .api.views import TraineeList_create,TraineeUpdate_delete

urlpatterns = [
    path('', TraineeListView.as_view(), name='trainee_list'),
     path('add/', TraineeAddView.as_view(), name='add_trainee'),
     path('update/<int:pk>/', TraineeUpdateView.as_view(), name='update_trainee'),
     path('details/<int:pk>/', TraineeDetailView.as_view(), name='trainee_details'),
     path('delete/<int:pk>/', TraineeDeleteView.as_view(), name='delete_trainee'),
     path('api/trainees/', TraineeList_create.as_view(), name='trainee-list-create'),
 path('api/trainees/<int:pk>/', TraineeUpdate_delete.as_view(), name='trainee-update-delete'),
]


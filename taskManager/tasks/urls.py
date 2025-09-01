
from django.urls import path
# from .views import task_detail, task_list
from .views import TaskDetail, TaskList

urlpatterns = [
    path('', TaskList.as_view(), name='task-list'),
    path('<int:pk>/', TaskDetail.as_view(), name='task-detail')
]





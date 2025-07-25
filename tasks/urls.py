from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/create_task', views.create_task, name='create_task'),
    path('tasks/<int:id>', views.task_details, name='task_details'),
    path('tasks/<int:id>/update', views.update_task, name='update_task'),
    path('tasks/<int:id>/delete', views.delete_task, name='delete_task'),
    path('tasks/<int:id>/toggle', views.toggle_task_status, name='toggle_task_status'),

    # NUEVAS RUTAS API
    path('api/tasks/', views.TaskListAPIView.as_view(), name='task_list_api'),
    path('api/tasks/<int:id>/', views.TaskDetailAPIView.as_view(), name='task_detail_api')
]
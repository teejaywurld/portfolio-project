from django.urls import path

from . import views

urlpatterns = [
    # path('', views.small_project),
    path('create/', views.create_project , name='create_projects'),
    path('get/', views.get_projects, name='view_all_projects'),
    path('filter/', views.filter_project),
    path('delete/<int:id>', views.delete_project, name='delete_projects'),
    path('get/<int:id>', views.retrieve_project, name='project_details'),
    path('update/<int:id>', views.update_project, name='update_projects'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_register , name = 'login_register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('piesapp/add/', views.create_pie, name='create_pie'),
    path('piesapp/allpies', views.all_pies, name='all_pies'),
    path('pie/<int:id>/', views.view_pie, name='view_pie'),
    path('edit_pie/<int:id>/', views.edit_pie, name='edit_pie'),  
    path('delete_pie/<int:id>/', views.delete_pie, name='delete_pie'),  
    path('logout', views.logout_view, name= 'logout'),
]

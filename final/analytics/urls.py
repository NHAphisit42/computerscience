from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_backend, name='home_backend'),
    path('table_student', views.table_backend, name='table_backend'),
    path('studentdetail/<int:id>', views.studentdetail, name='studentdetail'),
    path('remove/<int:id>', views.remove, name='remove'),
    path('login', views.login_backend, name='login_backend'),
    path('register', views.register_backend, name='register_backend'),
    path('adduser_backend', views.adduser_backend, name='adduser_backend'),
    path('sign_in', views.sign_in, name='sign_in'),
    path('logout_backend', views.logout_backend, name='logout_backend'),
    
    path('predictive', views.predictive, name='predictive'),
    path('result', views.result, name='result'),
    path('student_list', views.student_list, name='student_list'),
    
    path('clustering', views.cluster, name='clustering'),
    path('student_list_cluster', views.student_list_cluster, name='student_list_cluster'),
    path('result_cluster', views.result_cluster, name='result_cluster'),
    # path('admin', views.admin, name='admin')
]
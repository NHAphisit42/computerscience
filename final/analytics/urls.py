from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_backend, name='home_backend'),
    path('table_student', views.table_backend, name='table_backend'),
    path('studentdetail/<int:id>', views.studentdetail, name='studentdetail'),
    path('remove/<int:id>', views.remove, name='remove'),
    path('update', views.update, name='update'),
    path('chart_backend', views.chart_backend, name='chart_backend'),
    path('login', views.login_backend, name='login_backend'),
    path('register', views.register_backend, name='register_backend'),
    path('adduser_backend', views.adduser_backend, name='adduser_backend'),
    path('sign_in', views.sign_in, name='sign_in'),
    path('logout_backend', views.logout_backend, name='logout_backend'),
    path('Addschool', views.addschool_backend, name='addschool_backend')
]

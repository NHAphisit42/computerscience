from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_backend, name='home_backend'),
    path('table_student', views.table_backend, name='table_backend'),
    path('studentdetail/<int:id>', views.studentdetail, name='studentdetail'),
    path('remove/<int:id>', views.remove, name='remove'),
    path('chart_backend', views.chart_backend, name='chart_backend'),
    path('login', views.login_backend, name='login_backend'),
    path('register', views.register_backend, name='register_backend'),
    path('adduser_backend', views.adduser_backend, name='adduser_backend'),
    path('sign_in', views.sign_in, name='sign_in'),
    path('logout_backend', views.logout_backend, name='logout_backend'),
    path('Addschool', views.addschool_backend, name='addschool_backend'),
    path('addschool', views.addschool, name='add'),
    path('plan', views.plan, name='plan'),
    path('plan_detail/<int:id>', views.plandetail, name='plan_detail'),
    path('school', views.school, name='school'),
    path('education', views.education, name='education'),
    path('round_apply', views.round_apply, name='round_apply'),
    path('round_applydetail/<int:id>', views.round_applydetail, name='round_applydetail'),
    path('predictive', views.predictive, name='predictive'),
    path('result', views.result, name='result'),
    path('student_list', views.student_list, name='student_list'),
    path('schooldetail/<int:id>', views.schooldetail, name='schooldetail'),
    path('remove_school/<int:id>', views.delschool, name='remove_school'),
]
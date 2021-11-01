from django.urls import path
from userprofile import views
app_name = 'userprofile'
urlpatterns = [    
    # path('<int:question_id>/', views.detail, name='login'),    
    path('', views.detail, name='login'),    
    ]
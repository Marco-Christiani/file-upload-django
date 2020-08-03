from django.urls import path
from . import views

urlpatterns = [
   path('', views.Home.as_view(), name='home'), # Main Home View
   path('success/', views.Success.as_view()),
   path('upload/', views.Upload.as_view()),
   path('uploadfile/', views.upload_file),
   path('api/progress/', views.UploadProgress.as_view()),
]

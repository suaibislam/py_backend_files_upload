# from django.contrib import admin
# from django.contrib.auth import views as auth_views
# from django.urls import path
# from . import views
 
# urlpatterns = [
#     path('', views.formpage, name='home'),
#     path('uploadFiles', views.upload, name="upload-files")
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_and_display_files, name='upload_and_display'),
    
]
from django.urls import path
from cnab import views

urlpatterns = [
    path('insert_file/', views.FileView.as_view()),
]
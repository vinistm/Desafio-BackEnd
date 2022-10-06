from django.urls import path
from files import views

urlpatterns = [
    path('file/', views.ViewFile.as_view()),
]
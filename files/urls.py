from django.urls import path
from files import views

urlpatterns = [
    path('insert_values/', views.FileAll.as_view()),
]
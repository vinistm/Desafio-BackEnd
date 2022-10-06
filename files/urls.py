from django.urls import path
from files import views

urlpatterns = [
    path('insertvalues/', views.FileAll.as_view()),
]
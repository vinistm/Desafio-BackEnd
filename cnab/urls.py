from django.urls import path
from cnab import views

urlpatterns = [
    path('insertfile/', views.FileView.as_view()),
]
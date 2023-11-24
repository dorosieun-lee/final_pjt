from django.urls import path
from . import views

urlpatterns = [
    path('', views.quiz_list),
    path('<int:quiz_pk>/', views.quiz_detail)
]
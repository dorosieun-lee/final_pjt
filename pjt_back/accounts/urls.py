from django.urls import path
from accounts import views

urlpatterns = [
    path('userdetail/', views.userDetail_list),
    path('like_list/', views.like_list),
    path('withdraw/', views.delete_user),
    path('check_superuser/', views.check_superuser),
    path('checkUserID/', views.checkUserID)
]
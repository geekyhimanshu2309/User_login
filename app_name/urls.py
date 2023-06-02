from app_name import views
from django.urls import path

urlpatterns = [
    # Other URL patterns
    path('login/', views.login_view, name='login'),
]

from .views import login_view
from django.urls import path

urlpatterns = [
    # Other URL patterns
    path('login/', login_view, name='login'),
]

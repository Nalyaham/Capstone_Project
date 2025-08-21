from django.urls import path
from .views import ReviewView

urlpatterns = [
    path('movies/<int:movie_id>/reviews/', ReviewView.as_view()),
name = 'reviews']
from django.urls import path
from .views import ReviewView, RegisterView, submit_review, update_review, delete_review, search_reviews

urlpatterns = [
    path('movies/<int:movie_id>/reviews/', ReviewView.as_view()),
    path ('register/', RegisterView, name = 'register'),
    path('submit/', submit_review, name='submit'), 
    path('update/<int:pk>/reviews/', update_review, name='update'),
    path('delete/<int:pk>/reviews/', delete_review, name='delete'),
    path('search/', search_reviews, name='search'),
]
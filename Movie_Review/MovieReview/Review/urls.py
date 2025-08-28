from django.urls import path
from .views import ReviewView, RegistrationView,  submit_review, update_review, delete_review, search_reviews

urlpatterns = [
    path('movies/<int:movie_id>/reviews/', ReviewView.as_view()),
    path('register/', RegistrationView.as_view(), name = 'register'),
    path('submit0/', submit_review, name='submit0'), 
    path('update0/<int:pk>/reviews/', update_review, name='update0'),
    path('delete0/<int:pk>/reviews/', delete_review, name='delete0'),
    path('search/', search_reviews, name='search'),
    ]

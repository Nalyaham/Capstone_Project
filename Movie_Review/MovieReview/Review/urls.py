from django.urls import path
from .views import RegistrationView,  SubmitView, UpdateReview, DeleteReview, ListReview, TokenView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name = 'register'),
    path('submit/', SubmitView.as_view(), name='submit'), 
    path('reviews/<int:pk>/update/', UpdateReview.as_view(), name='update'),
    path('reviews/<int:pk>/delete/', DeleteReview.as_view(), name='delete'),
    path('reviews/', ListReview.as_view(), name='reviews'),
    path('token/', TokenView.as_view(), name='token'), ]

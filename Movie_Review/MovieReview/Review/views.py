from django.shortcuts import render, redirect 
from .models import Review, CustomUser
from .forms import ReviewForm, RegisterForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from .serializers import ReviewSerializer, UserSerializer
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import login
from rest_framework.response import Response
from rest_framework import generics 
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.db import IntegrityError
from rest_framework.exceptions import PermissionDenied

class RegistrationView(generics.CreateAPIView):
    queryset= CustomUser.objects.all()
    serializer_class= UserSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"detail": "Registration successful"})
        except IntegrityError:
            return Response({"error": "Username already exists"}, status=400)

@login_required
def submit_review(request):
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('review_detail')
        
class SubmitView(generics.CreateAPIView):
    queryset= Review.objects.all()
    serializer_class= ReviewSerializer

    def create(self, request, *args, **kwargs):
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"detail": "Submission successful"})
	
        
@login_required
def update_review(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if review.user != request.user:
        return redirect('home') 

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('review_detail', pk=pk)
    else:
        form = ReviewForm(instance=review)

    return render(request, 'update_review.html', {'form': form})


@login_required
def delete_review(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if review.user != request.user:
        return redirect('home') 

    if request.method == 'POST':
        review.delete()
        return redirect('home')  

    return render(request, 'delete_review.html', {'review': review})



class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000


class ReviewView(APIView):
    pagination_class = StandardResultsSetPagination


    def get(self, movie_id):
        reviews = Review.objects.filter(movie_id=movie_id)
        serializer = ReviewSerializer(reviews, many=True)
        paginator = self.pagination_class()
        return paginator.get_paginated_response(serializer.data)

    
def search_reviews(title=None, rating=None):
    movies = Review.objects.all()

    q = Q()

    if title:
        q &= Q(Movie_title__icontains=title)

    if rating:
        q &= Q(Rating=rating)

    movies = movies.filter(q)

    return movies 


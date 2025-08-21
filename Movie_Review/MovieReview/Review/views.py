from django.shortcuts import render, redirect 
from .models import Review, CustomUser
from .forms import RegisterForm, ReviewForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Review
from .serializers import ReviewSerializer
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from .models import Review

@login_required
def submit_review(request):
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('review_detail')	
        
@login_required
def update_review(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if review.user != request.user:
        return redirect('home')  # or some other view

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
        return redirect('home')  # or some other view

    if request.method == 'POST':
        review.delete()
        return redirect('home')  # or some other view

    return render(request, 'delete_review.html', {'review': review})

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000

class ReviewView(APIView):
    pagination_class = StandardResultsSetPagination


    def get(self, request, movie_id):
        reviews = Review.objects.filter(movie_id=movie_id)
        serializer = ReviewSerializer(reviews, many=True)
        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(reviews, request)
        return paginator.get_paginated_response(serializer.data)
    
def filter_reviews(title=None, rating=None):
    movies = Review.objects.all()

    q = Q()

    if title:
        q &= Q(Movie_title__icontains=title)

    if rating:
        q &= Q(Rating=rating)

    movies = movies.filter(q)

    return movies 
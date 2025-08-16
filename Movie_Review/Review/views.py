from django.shortcuts import render, redirect 
from .models import Review, CustomUser
from .forms import RegisterForm, ReviewForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

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



from django.shortcuts import render, get_object_or_404, redirect
from .models import Review
from .forms import ReviewCreateForm

def review_list(request):
    context = {
        'review_list': Review.objects.all(),
    }
    return render(request, 'reviews/review_list.html', context)

def review_detail(request, pk):
    context = {
        'review': Review.objects.get(pk=pk),
    }
    return render(request, 'reviews/review_detail.html', context)

def review_create(request):
    if request.method == 'GET':
        context = {
        'form': ReviewCreateForm()
        }
        return render(request, 'reviews/review_form.html', context)
    else:
        form = ReviewCreateForm(request.POST)
        form.save()
        return redirect('reviews:review_list')

def review_update(request, pk):
    review = Review.objects.get(pk=pk)
    form = ReviewCreateForm(request.POST or None, instance=review)
    if request.method == 'POST':
        form.save()
        return redirect('reviews:review_list')
    
    context = {
        'form': form
    }
    return render(request, 'reviews/review_form.html', context)

def review_delete(request, pk):
    review = Review.objects.get(pk=pk)
    context = {
        'review': review
    }
    if request.method == 'POST':
        review.delete()
        return redirect('reviews:review_list')
    return render(request, 'reviews/review_confirm_delete.html', context)
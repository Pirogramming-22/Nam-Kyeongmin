from django.urls import reverse
from django.shortcuts import render, redirect
from .models import Review

def review_list(request):
    reviews = Review.objects.all()
    context = {
        'reviews': reviews
    }
    return render(request, 'review/list.html', context)

def review_detail(request, pk):
    review = Review.objects.get(id=pk)
    context = {
        'review': review
    }
    return render(request, 'review/detail.html', context)

def review_create(request):
    if request.method == 'POST':
        review = Review.objects.create(
            poster = request.FILES['poster'],
            title = request.POST['title'],
            release = request.POST['release'],
            genre = request.POST['genre'],
            stars = request.POST['stars'],
            director = request.POST['director'],
            actor = request.POST['actor'],
            running_time = request.POST['running_time'],
            summary = request.POST['summary'],
        )
        return redirect(reverse('review:review_list'))
    return render(request, 'review/create.html')

def review_update(request, pk):
    exist_review = Review.objects.get(id=pk)
    if request.method == 'POST':
        poster = request.FILES.get('poster') or exist_review.poster
        title = request.POST.get('title')
        release = request.POST.get('release')
        genre = request.POST.get('genre')
        stars = request.POST.get('stars')
        director = request.POST.get('director')
        actor = request.POST.get('actor')
        running_time = request.POST.get('running_time')
        summary = request.POST.get('summary')
        exist_review.poster = poster
        exist_review.title = title
        exist_review.release = release
        exist_review.genre = genre
        exist_review.stars = stars
        exist_review.director = director
        exist_review.actor = actor
        exist_review.running_time = running_time
        exist_review.summary = summary
        exist_review.save()
        return redirect('review:review_detail', pk=exist_review.pk)
    
    context = {
        'review': exist_review
    }
    return render(request, 'review/update.html', context)

def review_delete(request, pk):
    if request.method == 'POST':
        review = Review.objects.get(id=pk)
        review.delete()
        return redirect('review:review_list')
    return redirect('review:review_list')
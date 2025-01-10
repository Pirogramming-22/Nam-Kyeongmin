from django.urls import reverse
from django.shortcuts import render, redirect
from .models import Review
from .forms import GenreForm

def review_list(request):
    reviews = Review.objects.all()
    context = {
        'reviews': reviews
    }
    return render(request, 'review/list.html', context)

def calc_running_time(running_time):
    total_time = int(running_time.replace('분', '').strip())
    hour = total_time // 60
    min = total_time % 60
    return f"{hour}시간 {min}분"
    
def review_detail(request, pk):
    review = Review.objects.get(id=pk)
    review.running_time = calc_running_time(review.running_time)
    context = {
        'review': review
    }
    return render(request, 'review/detail.html', context)

def review_create(request):
    if request.method == 'POST':
        genre_form = GenreForm(request.POST)
        if genre_form.is_valid():
            genre = genre_form.cleaned_data['genre']
        review = Review.objects.create(
            poster = request.FILES['poster'],
            title = request.POST['title'],
            release = request.POST['release'],
            genre = genre,
            stars = request.POST['stars'],
            director = request.POST['director'],
            actor = request.POST['actor'],
            running_time = request.POST['running_time'],
            summary = request.POST['summary'],
        )
        return redirect(reverse('review:review_list'))
    genre_for_get = GenreForm()
    return render(request, 'review/create.html', {'genre_form': genre_for_get})

def review_update(request, pk):
    exist_review = Review.objects.get(id=pk)
    if request.method == 'POST':
        poster = request.FILES.get('poster') or exist_review.poster
        title = request.POST.get('title')
        release = request.POST.get('release')
        genre = GenreForm(request.POST, instance=exist_review)
        stars = request.POST.get('stars')
        director = request.POST.get('director')
        actor = request.POST.get('actor')
        running_time = request.POST.get('running_time')
        summary = request.POST.get('summary')
        
        if genre.is_valid():
            store_genre = genre.cleaned_data['genre']
        exist_review.poster = poster
        exist_review.title = title
        exist_review.release = release
        exist_review.genre = store_genre
        exist_review.stars = stars
        exist_review.director = director
        exist_review.actor = actor
        exist_review.running_time = running_time
        exist_review.summary = summary
        exist_review.save()
        return redirect('review:review_detail', pk=exist_review.pk)
    
    genre_for_get = GenreForm(instance=exist_review)
    context = {
        'review': exist_review,
        'genre_form': genre_for_get,
    }
    return render(request, 'review/update.html', context)

def review_delete(request, pk):
    if request.method == 'POST':
        review = Review.objects.get(id=pk)
        review.delete()
        return redirect('review:review_list')
    return redirect('review:review_list')
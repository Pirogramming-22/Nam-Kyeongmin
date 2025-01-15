from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import Idea

def idea_list(request):
    how_to_order = request.GET.get('order')
    if not how_to_order:
        how_to_order = 'created_at'
    ideas = Idea.objects.all().order_by(how_to_order)
    context = {
        'ideas': ideas
    }
    return render(request, 'ideas/list.html', context)

def idea_detail(request, pk):
    idea = Idea.objects.get(id=pk)
    context = {
        'idea': idea
    }
    return render(request, 'ideas/detail.html', context)

def idea_create(request):
    if request.method == 'POST':
        idea = Idea.objects.create(
            title = request.POST['title'],
            image = request.FILES['image'],
            explain = request.POST['explain'],
            interest = request.POST['interest'],
            develop_tool = request.POST['develop_tool'],
        )
        return redirect(reverse('ideas:idea_list'))
    return render(request, 'ideas/create.html')

def idea_update(request, pk):
    exist_idea = Idea.objects.get(id=pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES.get('image') or exist_idea.image
        explain = request.POST.get('explain')
        interest = request.POST.get('interest')
        develop_tool = request.POST.get('develop_tool')
        
        exist_idea.title=title
        exist_idea.image=image
        exist_idea.explain = explain
        exist_idea.interest = interest
        exist_idea.develop_tool = develop_tool
        exist_idea.save()
        return redirect('ideas:idea_detail', pk=exist_idea.pk)
    
    context = {
        'idea': exist_idea,
    }
    return render(request, "ideas/update.html", context)

def idea_delete(request, pk):
    if request.method == 'POST':
        idea = Idea.objects.get(id=pk)
        idea.delete()
        return redirect("ideas:idea_list")
    return redirect("ideas:idea_list")
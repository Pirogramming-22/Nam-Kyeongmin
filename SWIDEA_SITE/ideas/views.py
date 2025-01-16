from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Idea
from .forms import IdeaForm

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
        'idea': idea,
    }
    return render(request, 'ideas/detail.html', context)

def idea_create(request):
    if request.method == 'GET':
        form = IdeaForm()
        context = {
            'form': form 
        }
        return render(request, 'ideas/create.html', context)
    else:
        form = IdeaForm(request.POST, request.FILES)
        if form.is_valid():
            create_idea = form.save()
        return redirect('ideas:idea_detail', pk=create_idea.pk)
        

def idea_update(request, pk):
    if request.method == 'GET':
        idea = Idea.objects.get(id=pk)
        form = IdeaForm(instance=idea)
        context = {
            'form': form,
            'pk': pk
        }
        return render(request, 'ideas/update.html', context)
    else:
        idea = Idea.objects.get(id=pk)
        form = IdeaForm(request.POST, request.FILES, instance=idea)
        if form.is_valid():
            form.save()
        return redirect('ideas:idea_detail', pk)

def idea_delete(request, pk):
    if request.method == 'POST':
        idea = Idea.objects.get(id=pk)
        idea.delete()
        return redirect("ideas:idea_list")
    return redirect("ideas:idea_list")

@csrf_exempt
def update_like(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        idea_id = data.get('like_idea_id')
        is_like = data.get('is_like')
        
        try:
            idea = Idea.objects.get(id=idea_id)
            idea.is_like = is_like
            idea.save()
            return JsonResponse({'success': True, 'is_like': idea.is_like, 'message': '관심 상태가 업데이트되었습니다.'})
        except Idea.DoesNotExist:
            return JsonResponse({'success': False, 'message': '관심 항목이 없습니다.'})
    return JsonResponse({'success': False, 'message': '잘못된 요청입니다.'}, status=400)

@csrf_exempt
def update_interest(request, idea_id):
    if request.method == 'POST':
        idea = Idea.objects.get(id=idea_id)
        action = request.POST.get('action')
        if action == 'plus':
            idea.interest += 1
        elif action == 'minus':
            idea.interest -= 1
        idea.save()
        return JsonResponse({"success": True, "update_interest": idea.interest})
    return JsonResponse({"success": False, "error": "Invalid request"}, status=400)
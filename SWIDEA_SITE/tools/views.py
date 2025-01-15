from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Tool

def tool_list(request):
    tools = Tool.objects.all()
    context = {
        'tools': tools
    }
    return render(request, 'tools/tool_list.html', context)

def tool_detail(request, pk):
    tool = Tool.objects.get(id=pk)
    context = {
        'tool': tool
    }
    return render(request, 'tools/tool_detail.html', context)

def tool_create(request):
    if request.method == 'POST':
        tool = Tool.objects.create(
            name = request.POST['name'],
            type = request.POST['type'],
            explain = request.POST['explain'],
        )
        return redirect(reverse('tools:tool_list'))
    return render(request, 'tools/tool_create.html')

def tool_update(request, pk):
    exist_tool = Tool.objects.get(id=pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        type = request.POST.get('type')
        explain = request.POST.get('explain')
        
        exist_tool.name = name
        exist_tool.type = type
        exist_tool.explain = explain
        exist_tool.save()
        return redirect('tools:tool_detail', pk=exist_tool.pk)
    context = {
        'tool': exist_tool,
    }
    return render(request, 'tools/tool_update.html', context)
    
def tool_delete(request, pk):
    if request.method == 'POST':
        tool = Tool.objects.get(id=pk)
        tool.delete()
        return redirect('tools:tool_list')
    return redirect('tools:tool_list')
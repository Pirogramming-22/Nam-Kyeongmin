from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Feed

# Create your views here.
def my_page(request):
    feed = Feed.objects.get(id=1)
    context = {
        'feed': feed,
    }
    return render(request, 'feeds/my_page.html', context)

@csrf_exempt
def like_ajax(request):
    if request.method == "POST":
        data = json.loads(request.body)
        feed_id = data.get('id')
            
        feed = Feed.objects.filter(id=feed_id).first()
        feed.like_count += 1
        feed.save()
            
        return JsonResponse({"like_count": feed.like_count})
    return JsonResponse({"error"}, status=400)
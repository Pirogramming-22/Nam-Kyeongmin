from django.shortcuts import render

# Create your views here.
def my_page(request):
    return render(request, 'feeds/my_page.html')
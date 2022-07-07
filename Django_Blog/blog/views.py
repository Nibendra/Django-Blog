from django.shortcuts import render

# Create your views here.
# Function-based view
def home(request):
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')

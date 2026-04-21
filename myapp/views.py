from django.shortcuts import render
from .models import FrontPageImage

def home(request):
    # Get the active front page image
    try:
        front_image = FrontPageImage.objects.filter(is_active=True).latest('created_at')
    except FrontPageImage.DoesNotExist:
        front_image = None
    
    context = {
        'front_image': front_image
    }
    return render(request, 'myapp/home.html', context)

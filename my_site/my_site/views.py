from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse("Home Page of Site")  # template html

from django.shortcuts import render

# Create your views here.
def my_index_site(request):
    return render(request, 'my_site.html', {})

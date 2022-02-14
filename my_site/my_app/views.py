from django.shortcuts import render
from django.http import HttpResponse


MyPages = {
    'index' : 'Index Page.',
    'about' : 'About Page.',
    'blog' : 'Blog Page.',
}

MyBlogCat = {
    'activities': 'Activities posts',
    'projects': 'Projects posts',
    'news' : 'News Post',
}
# Create your views here.
def index(request):
    return HttpResponse(MyPages['index'])  # template html

def about(request):
    return HttpResponse(MyPages['about'])

def blog(request,blogcat):
    return HttpResponse(MyBlogCat[blogcat])

def Blog_numpost(request,num1,num2):
    # domain.com/myapp/num1/num2 --> num1 + num2
    result = num1 + num2
    return HttpResponse(str(result))

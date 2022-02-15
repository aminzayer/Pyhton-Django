from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse


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

MyPostName ={
    'firstpost' :'This is my First Post.',
    'secondpost': 'This is my Second Post.',
    'thirdpost': 'This is my Third Post.',
}
# Create your views here.
def index(request):
    return render(request,'my_app/index.html')  # template .html

def about(request):
    return HttpResponse(MyPages['about'])

def blog(request,blogcat):
    return HttpResponse(MyBlogCat[blogcat])

def Blog_numpost(request,num1,num2):
    # domain.com/myapp/num1/num2 --> num1 + num2
    result = num1 + num2
    return HttpResponse(str(result))


def post_view(request, post):
    return HttpResponse(MyPostName[post])

# Redirect Routing
def num_post_view(request, num_post):
    list_post = list(MyPostName.keys())  # 'activities','projects','news'
    blogpost = list_post[num_post]
    webpage = reverse('post-page', args=[blogpost])
    return HttpResponseRedirect(webpage)

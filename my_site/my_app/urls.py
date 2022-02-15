from django.urls import path
from . import views

# My app : domain.com/my_app/
urlpatterns = [
    path('', views.index, name='index'),  # /my_app --> Project urls.py
    path('about/',views.about),
    path('blog/cat/<str:blogcat>',views.blog),
    path('blog/post/<int:num1>/<int:num2>',views.Blog_numpost),
    path('blog/<str:post>', views.post_view),
    path('blog/<int:num_post>',views.num_post_view),
]

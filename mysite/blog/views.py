from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse , Http404
from .models import Post

def all_posts (request):
    posts = Post.objects.all()
    return render(request=request , template_name='blog\post\list.html',context={'posts':posts})


def post_detail(request , id):
    #method 1
#     try :
#       post = Post.objects.get(id=id)
#     except Post.DoesNotExist :
#        raise Http404("No Post Found")
#     return render(request=request , template_name='',context={'post':post})

   #method 2
    post = get_object_or_404(Post,id=id,status = Post.Status.PUBLISHED)
    return render(request=request , template_name='blog\post\detail.html',context={'post':post})
from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse , Http404
from .models import Post
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger
def all_posts (request):
    Post_lists = Post.objects.all()
    paginator = Paginator(Post_lists, 3)
    page_number = request.GET.get('page',1)
    try:
       posts = paginator.page(page_number)
    except EmptyPage :
         posts = paginator.page(paginator.num_pages)
    except PageNotAnInteger :
         posts = paginator.page(1)
    return render(request=request , template_name='blog\post\list.html',context={'posts':posts})


def post_detail(request , year , month , day , slug):
    #method 1
#     try :
#       post = Post.objects.get(id=id)
#     except Post.DoesNotExist :
#        raise Http404("No Post Found")
#     return render(request=request , template_name='',context={'post':post})

   #method 2
    post = get_object_or_404(Post,
                             status = Post.Status.PUBLISHED,
                             slug = slug ,
                             published__year =  year,
                             published__month = month ,
                             published__day = day 
                             )
    return render(request=request , template_name='blog\post\detail.html',context={'post':post})
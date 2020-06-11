from django.shortcuts import render,get_object_or_404
from .models import Posts,Comment

# Create your views here.
def home (request):
    posts=Posts.objects.all()
    context={
        'title':'الصفحه الرئيسية',
        'posts':posts
    }
    return render(request,'blog/index.html',context)




def post_detail(request,id):
    post_detail=get_object_or_404(Posts,id=id)
    comment=post.comments.filter(active=True)

    context={
        'title':post_detail,
        "post_detail":post_detail,
        'comment':comment
        
    }
    return render(request,"blog/detail.html",context)

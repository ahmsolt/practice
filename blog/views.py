from django.shortcuts import render,get_object_or_404
from blog.models import Post
def blog_view(request):
    post = Post.objects.all()
    context = {'post':post}
    return render (request,'blog/blog-home.html',context)
def blog_single(request,pid):
    x1 = get_object_or_404(Post,pk=pid,status=1)
    context = {'x1':x1}
    return render (request,'blog/blog-single.html',context)
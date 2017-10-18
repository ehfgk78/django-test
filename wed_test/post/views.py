from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from post.models import Post


def post_list(request):
    # return HttpResponse("It's post_list")
    latest_post_list = Post.objects.all().order_by('-created_date')
    context = {
        'latest_post_list': latest_post_list,
    }
    return render(
        request,
        "post/post_list.html",
        context
    )


def post_detail(request, post_id):
    return render(
        request,
        "post/post_detail.html",
        context={
            'post': Post.objects.get(pk=post_id)
        }
    )

def post_create(request):
    # return HttpResponse("It's post_create.html")
    if request.method == 'POST':
        request.POST.
    return
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

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
    selected_post = get_object_or_404(Post, pk=post_id)
    return render(
        request,
        "post/post_detail.html",
        {'post': selected_post}
    )


def post_create(request):
    # return HttpResponse("It's post_create.html")
    photo = request.FILES.get('photo')
    content = request.POST.get('content')
    if request.method == 'POST' and photo:
        # print(request.POST)
        # print(request.FILES)
        Post.objects.create(
            photo=photo,
            content=content
        )
        return redirect('post_list')
    else:
        return render(request, 'post/post_create.html')


def post_delete(request, post_id):
    # return HttpResponse("It's post_delete")
    if request.method == 'POST':
        post = Post.objects.get(pk=post_id)
        post.delete()
        return redirect('post_list')
    return redirect('post_detail', post_id=post_id)

from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
from datetime import datetime
from django.http import HttpResponseRedirect
from django.http import HttpResponse

def postpage(request, page_num):
    numOfPostsPerPage = 20
    tempNum = (page_num-1) * numOfPostsPerPage
    tempPosts = []
    for i in range(0, len(Post.objects.all())):
        tempPosts.append(Post.objects.all()[i])

    tempPosts.reverse()
    tempPosts2 = tempPosts[tempNum:tempNum+numOfPostsPerPage]
    if page_num == 1:
        return render(request, 'post/viewAllPosts.html', {"posts": tempPosts2, 'pre_page': 1, 'next_page': page_num+1, 'page_num': page_num})
    else:
        return render(request, 'post/viewAllPosts.html', {"posts": tempPosts2, 'pre_page': page_num-1, 'next_page': page_num+1, 'page_num': page_num})

# def ViewPost(request, post_id):
#     return render(request, 'post/viewPostIndex.html', {"selectedPost": Post.objects.get(id = post_id)})

# class IndexView(generic.ListView):
#     template_name = 'post/viewAllPosts.html'
#     context_object_name = 'userPost'
    
#     def get_queryset(self):
#         return reversed(Post.objects.all()[:15])

class DetailView(generic.DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'post/viewPostIndex.html'


def SearchPost(request, page_num):
    target_author = request.POST["target_author"]
    targetPosts = Post.objects.filter(author__contains=target_author)
    targetPosts = reversed(targetPosts)

    if page_num == 1:
        return render(request, 'post/viewAllPosts.html', {"posts": targetPosts, 'pre_page': 1, 'next_page': page_num+1, 'page_num': page_num})
    else:
        return render(request, 'post/viewAllPosts.html', {"posts": targetPosts, 'pre_page': page_num-1, 'next_page': page_num+1, 'page_num': page_num})

class AddNewPost(CreateView):
    model = Post
    template_name = 'post/posting.html'
    fields = {'subject', 'author', 'content'}

class UpdatePost(UpdateView):
    model = Post
    template_name = 'post/editing.html'
    fields = {'subject', 'author', 'content'}

class DeletePost(DeleteView):
    model = Post
    success_url = '/post/1'
    
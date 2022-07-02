from django.views import generic
from .models import Post, about

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

class about(generic.DetailView):
    model = about
    template_name = 'about.html'
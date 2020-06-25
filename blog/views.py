from django.shortcuts import render
from .models import post
from django.views import generic

def home(request):
    return render(request, "home.html", context=None)

class postlist(generic.ListView):
    queryset = post.objects.filter(status=1).order_by('-created_on')
    template_name = 'post.html'
    paginate_by = 3

class postdetail(generic.DetailView):
    model = post
    template_name = 'post_detail.html'

from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Article

def index(request):

    latest_article_list = Article.objects.order_by('pub_date')
    return render(request, 'bercoon/list.html', {'latest_article_list':latest_article_list})

def detail(request, article_id):
    try:
        a = Article.objects.get( id = article_id)
    except:
        raise Http404('Cnfnmz yt yfqltyf')
    latest_comment_list = a.comment_set.order_by('-id')[:10]

    return render(request, 'bercoon/detail.html', {'article':a, 'latest_comment_list':latest_comment_list})

def leave_comment(request, article_id):
    try:
        a = Article.objects.get( id = article_id)
    except:
        raise Http404('Cnfnmz yt yfqltyf')

    a.comment_set.create(autor_name = request.POST['name'], comment_text = request.POST['text'])

    return HttpResponseRedirect(reverse('bercoon:detail', args=(a.id,)))
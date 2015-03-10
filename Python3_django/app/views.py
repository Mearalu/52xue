# Create your views here.
from django.template import loader,Context
from django.http import HttpResponse
from app.models import appPost
def archive(request):
    posts=appPost.objects.all()
    posts
    t=loader.get_template("archive.html")
    c=Context({'posts':posts})
    c['year']='2015'
    c['title']='djiango 吾爱学'
    return HttpResponse(t.render(c))
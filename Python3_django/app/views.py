# Create your views here.
from django.template import loader,Context
from django.http import HttpResponse
from app.models import appPost
def archive(request):
    posts=appPost.objects.all()
    t=loader.get_template("archive.html")
    c=Context({'posts':posts})
    return HttpResponse(t.render(c))
from django.shortcuts import render,render_to_response

from django.http import HttpResponseRedirect, HttpResponse
from bbs.models import *
# Create your views here.



def index(request):

	return render_to_response('index.html')

def python_bbs(request):
	bbs_list = bbs.objects.all()
	return render_to_response('blog.html', {'bbs_list': bbs_list})

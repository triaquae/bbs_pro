from django.shortcuts import render,render_to_response

from django.http import HttpResponseRedirect, HttpResponse
from bbs.models import *
# Create your views here.



def index(request):

	return render_to_response('index.html')

def python_bbs(request):
	bbs_list = bbs.objects.all()
	return render_to_response('blog.html', {'bbs_list': bbs_list})


def bbs_detail(request):
	print len(request.POST),request.POST
	if len(request.POST) != 0:
		bbs_id =  request.POST['BBS_ID'].split('_')[1]
		bbs_obj = bbs.objects.get(id = bbs_id)
		print bbs_obj
		return render_to_response('bbs_detail.html', {'bbs_obj':bbs_obj})
	else:
		bbs_list = bbs.objects.all()
		return render_to_response('blog.html', {'bbs_list': bbs_list})

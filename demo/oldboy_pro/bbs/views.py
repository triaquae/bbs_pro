from django.shortcuts import render,render_to_response, RequestContext

from django.http import HttpResponseRedirect, HttpResponse
from bbs.models import *
from django.contrib import comments 
# Create your views here.
import datetime


def index(request):

	return render_to_response('index.html')

def python_bbs(request):
	bbs_list = bbs.objects.all()
	return render_to_response('blog.html', {'bbs_list': bbs_list},context_instance=RequestContext(request))

def add_comment(request):
	print request.GET
	name,email,msg = request.GET['name'], request.GET['email'], request.GET['message']
	bbs_id = request.GET['bbs_id']
	a=comments.models.Comment.objects.create(content_type_id = 9, object_pk=bbs_id, site_id=1, user_name=name,user_email=email, comment= msg ,submit_date=datetime.datetime.now())
	a.save()
	bbs_obj = bbs.objects.get(id = bbs_id)
	
	return render_to_response('bbs_detail.html', {'bbs_obj':bbs_obj})
def bbs_detail(request):
	print len(request.POST),request.POST
	if len(request.POST) != 0:
		bbs_id =  request.POST['BBS_ID'].split('_')[1]
		bbs_obj = bbs.objects.get(id = bbs_id)
		print bbs_obj.author.signature,bbs_obj.id
		return render_to_response('bbs_detail.html', {'bbs_obj':bbs_obj})
	else:
		bbs_list = bbs.objects.all()
		return render_to_response('blog.html', {'bbs_list': bbs_list})

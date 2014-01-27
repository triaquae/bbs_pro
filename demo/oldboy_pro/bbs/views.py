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
	#return render_to_response('blog.html', {'bbs_list': bbs_list})

def add_comment(request):
	print request.GET
	parent_comment_id = ''
	name,email,msg = request.GET['name'], request.GET['email'], request.GET['message']

	if request.GET.has_key('comment_id'):parent_comment_id = request.GET['comment_id']
	bbs_id = request.GET['bbs_id']
	a=comments.models.Comment.objects.create(content_type_id = 9, object_pk=bbs_id, ip_address= parent_comment_id,  site_id=1, user_name=name,user_email=email, comment= msg ,submit_date=datetime.datetime.now())
	a.save()
	bbs_obj = bbs.objects.get(id = bbs_id)
	
	return render_to_response('bbs_detail.html', {'bbs_obj':bbs_obj})

def add_agree(request):
	bbs_id = request.POST['bbs_id']
	bbs_obj = bbs.objects.get(id = bbs_id)
	if request.POST['agree'] == 'YES':
		bbs_obj.agree_count += 1
	else:
		bbs_obj.agree_count -= 1
	bbs_obj.save()
	print bbs_id,'||||'
	return HttpResponse( bbs_obj.agree_count )
def bbs_detail(request):
	print len(request.POST),request.POST
	
	if len(request.POST) != 0:
		bbs_id =  request.POST['BBS_ID'].split('_')[1]
		bbs_obj = bbs.objects.get(id = bbs_id)
		bbs_comments = comments.models.Comment.objects.filter(object_pk= bbs_id)
		print bbs_comments
		bbs_obj.view_count += 1
		bbs_obj.save()
		return render_to_response('bbs_detail.html', {'bbs_obj':bbs_obj, 'bbs_comments': bbs_comments})
	else:
		bbs_list = bbs.objects.all()
		return render_to_response('blog.html', {'bbs_list': bbs_list})

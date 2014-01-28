from django.shortcuts import render,render_to_response, RequestContext

from django.http import HttpResponseRedirect, HttpResponse
from bbs.models import *
from django.contrib import comments 
# Create your views here.
import datetime,time


new_comment_dic ={}



def index(request):

	return render_to_response('index.html')

def python_bbs(request):
	bbs_list = bbs.objects.all()
	return render_to_response('blog.html', {'bbs_list': bbs_list},context_instance=RequestContext(request))
	#return render_to_response('blog.html', {'bbs_list': bbs_list})

def add_comment(request):
	print request.POST
	s=request.session
	print s._session_key,'============',request.COOKIES['sessionid']
	parent_comment_id = ''
	name,email,msg = request.POST['name'], request.POST['email'], request.POST['message']
	
	if request.POST.has_key('comment_id'):parent_comment_id = request.POST['comment_id']  #this comment is a child comment 
	bbs_id = request.POST['bbs_id']
	
	print new_comment_dic

	if new_comment_dic.has_key(s._session_key):
		time_diff = time.time() - new_comment_dic[ s._session_key ]
		if time_diff >30:
			a=comments.models.Comment.objects.create(content_type_id = 9, object_pk=bbs_id, ip_address= parent_comment_id,  site_id=1, user_name=name,user_email=email, comment= msg ,submit_date=datetime.datetime.now())
			a.save()
	                new_comment_dic[s._session_key]  = time.time() #add a new comment mark or renew the time stamp  
		else:
			print "need to send a comment after %s seconds" % time_diff
                        return HttpResponse("need to send a comment after %s seconds" % time_diff)
	else:  #first time submit the comment
		new_comment_dic[s._session_key]  = time.time() #add a new comment mark or renew the time stamp  
		a=comments.models.Comment.objects.create(content_type_id = 9, object_pk=bbs_id, ip_address= parent_comment_id,  site_id=1, user_name=name,user_email=email, comment= msg ,submit_date=datetime.datetime.now())
		a.save()

	bbs_obj = bbs.objects.get(id = bbs_id)
	bbs_comments = comments.models.Comment.objects.filter(object_pk= bbs_id)
	return render_to_response('bbs_detail.html', {'bbs_obj':bbs_obj, 'bbs_comments': bbs_comments})

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

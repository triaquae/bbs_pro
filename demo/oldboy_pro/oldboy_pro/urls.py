from django.conf.urls import patterns, include, url

from django.contrib import admin
from bbs.views import *

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'oldboy_pro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    (r'^accounts/login/$', 'django.contrib.auth.views.login',{'template_name': 'login.html'}),
    url(r'^admin/', include(admin.site.urls)),
     (r'^account_login/$',account_login), 
     (r'^login/$',login), 
     (r'^logout/$',logout), 

	(r'^$', index),
	(r'^python/$', python_bbs),
	(r'^linux/$', linux_bbs),
	(r'^diary/$', diary),
	(r'^jobs/$', jobs),
	(r'^bbs_detail/$', bbs_detail),
	(r'^addcomment/$', add_comment),
	(r'^add_agree/$', add_agree),
	(r'^personal_info/$', personal_info),
	(r'^upload_pic/$', upload_pic),
	(r'^add_new_article/$', add_new_article),
	(r'^new_article/$', new_article),
	(r'^get_bbs_content/(\d+)/$', get_bbs_content),
	(r'^get_data/$', get_data),
	
)

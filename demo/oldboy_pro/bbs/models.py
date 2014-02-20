from django.db import models
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
# Create your models here.



class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()
class web_user(models.Model):
    user = models.ForeignKey(User, null=True)
    email = models.EmailField()        
    class_name = models.ForeignKey('class_list')
    photo_height=models.PositiveIntegerField()
    photo_width=models.PositiveIntegerField() 
    photo = models.ImageField(upload_to="upload_imgs/" ,height_field="photo_height",width_field="photo_width", default="upload_imgs/user-1.jpg") 
    signature = models.CharField(max_length=150,default="lazy guy, got nothing left here...")
    def __unicode__(self):
        return '%s' % self.user

class class_list(models.Model):
        name = models.CharField(max_length=50, unique=True)
        def __unicode__(self):
                return self.name


class bbs(models.Model):
	title = models.CharField(max_length=100,unique=True)
	color = (('#E1F5A9', 'light-yellow'),('#FA8258', 'orange'), ('#81F7F3', 'sky-blue'),('#BEF781','light-green'), ('#E6E6E6','gray'),('#F6CEF5','pink'))
    	color_type = models.CharField(max_length=100, choices= color, default=None)
	choice = (('linux', 'Linux-bbs'),('python', 'Python-bbs'), ('diary','Diary'),('hiring', 'Hiring-bbs'))
    	category = models.CharField(max_length=100, choices= choice)
	publish_date = models.DateTimeField() 	
	author = models.ForeignKey(web_user)
	content = models.TextField()
	#order = models.IntegerField(default=-1)
	comment_count = models.IntegerField(default=0)
	view_count = models.IntegerField(default=0)
	agree_count = models.IntegerField(default=0)
	
	def __unicode__(self):
		return self.title

class new_bbs_form(ModelForm):
	class Meta:
		model = bbs
		fields = ('title','color_type','category')

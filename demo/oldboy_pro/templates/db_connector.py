#!/usr/bin/env python
#Author: Alex Li
import sys,os
sys.path.append('/var/www/sites/saltflakes.net/bbs_pro/demo/oldboy_pro')
os.environ['DJANGO_SETTINGS_MODULE'] ='oldboy_pro.settings'
#----------------Use Django Mysql model----------------
from bbs.models import * 

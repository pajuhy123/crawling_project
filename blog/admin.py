#blog/ admin.py
from django.contrib import admin


###########
from .models import CrawlingData
from .models import Post


###########
admin.site.register(CrawlingData)
admin.site.register(Post)
########

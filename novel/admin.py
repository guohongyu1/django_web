from django.contrib import admin
from novel import models
# Register your models here.
admin.site.register(models.Novel)
admin.site.register(models.WordCount)
admin.site.register(models.Status)
admin.site.register(models.BookTitle)
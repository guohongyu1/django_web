from django.contrib import admin

# Register your models here.
from app import models
admin.site.register(models.BxSlider)
admin.site.register(models.notice)
admin.site.register(models.Reinr)
admin.site.register(models.Direction)
admin.site.register(models.Classification)
admin.site.register(models.Level)
admin.site.register(models.video)
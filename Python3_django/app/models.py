from django.db import models
from django.contrib import admin

# Create your models here.
class appPost(models.Model):
    title=models.CharField(max_length=150)
    body=models.TextField()
    timestamp=models.DateTimeField()
    #��ʱ�䵹������
    class Meta:
        ordering=('-timestamp',)
class appPostAdmin(admin.ModelAdmin):
    list_display=('title','timestamp')
admin.site.register(appPost,appPostAdmin)
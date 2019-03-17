from django.db import models

# Create your models here.
class BookTitle(models.Model):
    title=models.CharField(max_length=32)
    class Meta:
        db_table='BookTitle'
        verbose_name_plural='分类'
    def __str__(self):
        return self.title
class WordCount(models.Model):
    count_choice=((0,'30万字以下'),
                  (1, '30-50万字'),
                  (2,'50-100万字'),
                  (3, '100-200万字'),
                  (4, '200万字以上'),
                  )
    status=models.IntegerField(choices=count_choice)
class Status(models.Model):
    status=models.CharField(max_length=12)
class Chapter(models.Model):
    section=models.CharField(max_length=64)
    content = models.TextField()
class Novel(models.Model):
    name=models.CharField(max_length=32)
    href=models.CharField(max_length=255)
    author=models.CharField(max_length=32)
    count = models.CharField(max_length=64)
    book_intro=models.TextField()
    img = models.ImageField(verbose_name='图片', upload_to='../static/bookimg')
    status = models.ForeignKey('Status', null=True, blank=True, on_delete=models.CASCADE)
    chapter=models.ForeignKey('Chapter',null=True,blank=True,on_delete=models.CASCADE)
    wordcount = models.ForeignKey('WordCount', null=True, blank=True, on_delete=models.CASCADE)
    booktitle = models.ForeignKey('BookTitle', null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
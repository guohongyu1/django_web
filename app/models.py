from django.db import models


# Create your models here.
class BxSlider(models.Model):
    status_choice=(
        (0,'下线'),
        (1,'上线'),
    )
    status=models.IntegerField(choices=status_choice,default=1)
    name=models.CharField(max_length=32,unique=True)
    img=models.ImageField(upload_to='./static/img/')
    href=models.CharField(max_length=256)
    create_date=models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table='BxSlider'
        verbose_name_plural='首页轮播'
    def  __str__(self):
        return self.name
class notice(models.Model):
    status_choice=(
        (0,'下线'),
        (1,'上线'),
    )

    status=models.IntegerField(choices=status_choice,default=1)
    weight = models.IntegerField(verbose_name='权重（按从大到小排列）', default=0)
    name=models.CharField(max_length=32 ,unique=True)
    data1=models.CharField(max_length=500)
    data2=models.CharField(max_length=1000)
    href=models.CharField(max_length=256)
    create_date=models.DateTimeField(auto_now_add=True)
    class Meta():
        db_table='公告'
    def __str__(self):
        return self.name
class Reinr(models.Model):
    name=models.CharField(max_length=32)
    # contentInt=models.CharField(max_length=256)
    img = models.FileField(upload_to='static/img',max_length=256)
    # href=models.CharField(max_length=256,)
    # class Meta():
    #     db_table='资源介绍'
    def __str__(self):
        return self.name
class Direction(models.Model):
    weight=models.IntegerField(verbose_name='权重(从大到小排列)')
    name=models.CharField(max_length=32)
    classification=models.ManyToManyField('Classification')
    level=models.ManyToManyField('Level')
    class Meta:
        db_table='Direction'
        verbose_name_plural='方向'
    def __str__(self):
        return self.name
class Classification(models.Model):
    name=models.CharField(max_length=32)
    weight=models.IntegerField(verbose_name='权重(从大到小排列)')
    class Meta:
        db_table='Classfication'
        verbose_name_plural='分类'
    def __str__(self):
        return self.name
class Level(models.Model) :
    title=models.CharField(max_length=32)
    class Meta:
        verbose_name_plural='级别'
    def __str__(self):
        return self.title
class video(models.Model):
    status_choice=(
        (0,'下线'),
        (1,'上线')
    )
    status=models.IntegerField(verbose_name='状态',choices=status_choice,default=1)
    level=models.ForeignKey('Level',null=True,blank=True,on_delete=models.CASCADE)
    direction=models.ForeignKey('Direction',null=True,blank=True,on_delete=models.CASCADE)
    classification=models.ForeignKey('Classification',null=True,blank=True,on_delete=models.CASCADE)
    title=models.CharField(max_length=32)
    summary=models.CharField(max_length=32)
    img=models.ImageField(verbose_name='图片',upload_to='../static/video/')
    href=models.CharField(verbose_name='视频地址',max_length=256)
    create_date=models.DateTimeField(auto_now_add=True)
    class Meda:
        db_table='video'
        verbose_name_plural='视频'
    def __str__(self):
        return self.title




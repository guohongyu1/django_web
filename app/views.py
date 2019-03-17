from django.shortcuts import render
from app import models
from django.http import JsonResponse
import json
# Create your views here.
def index(request,**kwargs):
    for k,v in kwargs.items():
        kwargs[k]=int(v)
    classification_id=kwargs.get('classification_id')
    print(classification_id)
    list_classification = models.Classification.objects.all()
    list_img=models.BxSlider.objects.all()
    video_list = models.video.objects.order_by('-create_date').values('title','img','href')[:10]
    l=[i for i in range(1,len(list_img)+1)]
    return render(request,'index.html',locals())
def get_notice(request):
    nid=request.GET.get('nid')
    list_notice = models.notice.objects.filter(id=nid).values("id","data1")
    ret={
        "data":list(list_notice)
    }
    return JsonResponse(ret)
def video(request,*args,**kwargs):
    condition={}
    for k,v in kwargs.items():
        kwargs[k]=int(v)
    direction_id=kwargs.get('direction_id')
    classification_id=kwargs.get('classification_id')
    level_id = kwargs.get('level_id')
    list_direction = models.Direction.objects.all()
    # video_name = models.video.objects.filter(direction_id=1)
    # print(video_name)
    if direction_id == 0:
        list_classification = models.Classification.objects.all()
        if classification_id==0:
            pass
            # if level_id==0:
            #     pass
            # else:
            #     condition['level_id']=level_id
        else:
            if level_id==0:
                condition['classification_id'] = classification_id
            else:
                condition['classification_id'] = classification_id
                condition['level_id']=level_id
    else:
        direction_obj=models.Direction.objects.filter(id=direction_id).first()
        list_classification=direction_obj.classification.all()
        # list_level=direction_obj.level.all()
        vlist=direction_obj.classification.all().values_list('id')
        print(vlist)
        # llist=direction_obj.level.all().values_list('id')
        if  not vlist :
            classification_id_list=[]
            # level_id_list=[]
        else:
            classification_id_list=list(zip(*vlist))[0]
            print(classification_id_list)
            print(list(zip(*vlist)))
            # level_id_list=list(zip(zip(*llist)))[0]
            # condition['classification_id']=classification_id
            # condition['level_id'] = level_id
        if classification_id==0:
            # pass
            # if direction_id in id_direction:
            # video_name = models.video.objects.filter(direction_id=direction_id)
            #     condition['classification_id__in']=classification_id_list
            condition['direction_id']=direction_id
            # else:
            #     classification_id_list = []
            # condition['level_id__in'] = level_id_list
        else:
            if classification_id in classification_id_list:
                condition['direction_id'] = direction_id
                condition['classification_id']=classification_id
            else:
                kwargs['classification_id']=0
                condition['direction_id'] = direction_id
                # condition['classification_id__in']=classification_id_list
    if level_id==0:
        pass
    else:
        condition['level_id']=level_id
    list_level=models.Level.objects.all()
    list_video=models.video.objects.filter(**condition)
    return render(request,'video.html',
                  {
                      'kwargs':kwargs,
                      'list_direction':list_direction,
                      'list_classification':list_classification,
                      'list_level':list_level,
                      'list_video':list_video,
                })
# def imgs(request):
#     # img_list = models.Img.objects.all()
#     return render(request,'img.html')
def get_img(request):
    nid = request.GET.get('nid')
    img_list = models.Reinr.objects.filter(id__gt=nid).values('id','img','name')
    img_list = list(img_list)
    ret = {
        'status': True,
        'data': img_list
    }
    # return HttpResponse(json.dumps(ret))
    return JsonResponse(ret)
def imgs(request):
    list_img = models.BxSlider.objects.all()
    return render(request,'img.html',locals())

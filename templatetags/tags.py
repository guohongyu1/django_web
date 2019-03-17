from django.template import Library
from django.utils.safestring import mark_safe
register=Library()
@register.simple_tag
def get_date(notice):
    s=''
    data=notice.data1[:10]
    s+='<h6 class=%s>%s</h6>'%(notice.id,data)
    s+='<a name=%s class="get">查看更多</a>'%notice.id
    return mark_safe(s)
@register.simple_tag
def get_num(video,video_list):
    return list(video_list).index(video)+1
from django.shortcuts import render
from novel import models
# Create your views here.
def novel(request):
    cur_page=request.GET.get('_page')
    print(cur_page)
    books=models.Novel.objects.values('name','href','author','count','img','book_intro')
    types=models.BookTitle.objects.all()
    status=models.Status.objects.all()
    wordcount=models.WordCount.objects.all()
    start=(int(cur_page)-1)*6
    cur_books=books[start:start+6]
    l=len(books)//6+1
    s=[i for i in range(1,l+1)]
    return render(request,'book.html',locals())

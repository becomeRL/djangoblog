from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Memo, KorTexts, EngTexts, NewsData, Photo

# Create your views here.

def index(req):
    return render(req, 'blog_app/index.html')

def home(req):
    kor_scrapelist = KorTexts.objects.all()
    eng_scrapelist = EngTexts.objects.all()
    news_scrapelist = NewsData.objects.all()
    return render(req, 'blog_app/home.html', {'kor_scrapelist':kor_scrapelist, 'eng_scrapelist':eng_scrapelist, 'news_scrapelist':news_scrapelist})

def memo(req):
    memolist = Memo.objects.all()
    return render(req, 'blog_app/memo.html', {'memolist':memolist})

def detail_memo(req, pk):
    memo = Memo.objects.get(pk=pk)
    return render(req, 'blog_app/detail_memo.html', {'memo':memo})

def new_memo(req):
    if req.method == 'POST':
        memo = Memo()
        memo.title = req.POST['title']
        memo.body = req.POST['body']
        memo.pub_date = timezone.now()
        memo.save()
        for img in req.FILES.getlist('image'):
            photo = Photo()
            photo.memo = memo
            photo.image = img
            photo.save()
        # memo.image = req.FILES.get('image')
        return redirect('/memo/')
    return render(req, 'blog_app/new_memo.html')

def remove_memo(req, pk):
    memo = Memo.objects.get(pk=pk)
    if req.method == 'POST':
        memo.delete()
        return redirect('/memo/')
    return render(req, 'blog_app/remove_memo.html', {'Memo':memo})

def update_memo(req, pk):
    memo = Memo.objects.get(pk=pk)

    if req.method == 'POST':
        memo.title = req.POST['title']
        memo.body = req.POST['body']
        memo.pub_date = timezone.now()
        memo.save()
        for img in req.FILES.getlist('image'):
            photo = Photo()
            photo.memo = memo
            photo.image = img
            photo.save()
        return redirect('/memo/')
    return render(req, 'blog_app/update_memo.html', {'Memo':memo})

def test(req):
    return render(req, 'blog_app/test.html')

def search(req):
    memos = Memo.objects.all().order_by('-id')
    q = req.POST.get('q',"")
    if q:
        memos = memos.filter(title__icontains=q)
        return render(req, 'blog_app/search.html', {'memos':memos,'q':q})
    else:
        return render(req, 'blog_app/search.html')
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Memo, KorTexts, EngTexts

# Create your views here.

def index(req):
    return render(req, 'blog_app/index.html')

def home(req):
    kor_scrapelist = KorTexts.objects.all()
    eng_scrapelist = EngTexts.objects.all()
    return render(req, 'blog_app/home.html', {'kor_scrapelist':kor_scrapelist, 'eng_scrapelist':eng_scrapelist})

def memo(req):
    memolist = Memo.objects.all()

    return render(req, 'blog_app/memo.html', {'memolist':memolist})

def detail_memo(req, pk):
    memo = Memo.objects.get(pk=pk)

    return render(req, 'blog_app/detail_memo.html', {'memo':memo})

def new_memo(req):
    if req.method == "POST":
        new_article = Memo.objects.create(
            title=req.POST['title'],
            pub_date=timezone.now(),
            body=req.POST['body'],
        )
        return redirect('/memo/')
    return render(req, 'blog_app/new_memo.html')

def remove_memo(req, pk):
    memo = Memo.objects.get(pk=pk)
    if req.method == 'POST':
        memo.delete()
        return redirect('/memo/')
    return render(req, 'blog_app/remove_memo.html', {'Memo':memo})

import requests
from bs4 import BeautifulSoup
import json
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog_project.settings")

import django

django.setup()

from blog_app.models import KorTexts, EngTexts, NewsData

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def parse_conv():
    KorTexts.objects.all().delete()
    EngTexts.objects.all().delete()
    req = requests.get('https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    today_texts = soup.select(
        '.conv_sub > b'
    )
    ko_texts = {}
    en_texts = {}

    for index, title in enumerate(today_texts):
        if index < 4 :
            ko_texts[index] = title.text

        elif index >= 4:
            en_texts[index] = title.text


    ko_texts_value = ko_texts.values()
    en_texts_value = en_texts.values()

    return (ko_texts_value, en_texts_value)

def parse_news():
    NewsData.objects.all().delete()
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'}
    req = requests.get('https://news.naver.com/', headers=headers)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    today_newses = soup.select(
        '#today_main_news > div.hdline_news > ul > li > div.hdline_article_tit'
    )
    newses_links = soup.select(
        '#today_main_news > div.hdline_news > ul > li > div.hdline_article_tit > a'
    )
    hdline_news = {}
    hdline_news_links = {}

    for index, news in enumerate(today_newses):
        hdline_news[index] = news.text
    for index, link in enumerate(newses_links):
        hdline_news_links[index] = 'https://news.naver.com' + link.get('href')

    hdline_news_value = hdline_news.values()
    hdline_news_links_value = hdline_news_links.values()

    return (hdline_news_value, hdline_news_links_value)

if __name__ == "__main__":
    conv = parse_conv()
    for k in conv[0]:
        KorTexts(ko_text=k).save()
    for e in conv[1]:
        EngTexts(en_text=e).save()

    news = parse_news()
    for t in news[0]:
        NewsData(title=t).save()
    for l in news[1]:
        NewsData(link=l).save()
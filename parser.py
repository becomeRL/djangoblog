import requests
from bs4 import BeautifulSoup
import json
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog_project.settings")

import django

django.setup()

from blog_app.models import KorTexts, EngTexts

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def parse_blog():

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
    # return data.values()

if __name__ == "__main__":
    conv = parse_blog()
    for k in conv[0]:
        KorTexts(ko_text=k).save()
    for e in conv[1]:
        EngTexts(en_text=e).save()
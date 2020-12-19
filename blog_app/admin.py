from django.contrib import admin
from .models import Memo, KorTexts, EngTexts, NewsData, NewsLink, Photo
# Register your models here.

class PhotoInline(admin.TabularInline):
    model = Photo
class MemoAdmin(admin.ModelAdmin):
    inlines = [PhotoInline, ]

admin.site.register(Memo, MemoAdmin)
admin.site.register(KorTexts)
admin.site.register(EngTexts)
admin.site.register(NewsData)
admin.site.register(NewsLink)
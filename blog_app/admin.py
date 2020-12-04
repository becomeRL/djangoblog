from django.contrib import admin
from .models import Memo, KorTexts, EngTexts
# Register your models here.

admin.site.register(Memo)
admin.site.register(KorTexts)
admin.site.register(EngTexts)
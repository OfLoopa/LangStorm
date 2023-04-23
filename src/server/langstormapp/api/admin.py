from django.contrib import admin
from .models import Word, DictionaryRecord, Lesson

admin.site.register(Word)
admin.site.register(DictionaryRecord)
admin.site.register(Lesson)


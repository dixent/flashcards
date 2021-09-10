from django.contrib import admin

from .models import Card, Language

class CardAdmin(admin.ModelAdmin):
    list_display = ('text', 'translation', 'learning_index')

admin.site.register(Card, CardAdmin)
admin.site.register(Language)

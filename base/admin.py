from django.contrib import admin

# Register your models here.

from.models import Author, Title

admin.site.register(Author)
# admin.site.register(Curiosity)
# admin.site.register(Comment)
admin.site.register(Title)

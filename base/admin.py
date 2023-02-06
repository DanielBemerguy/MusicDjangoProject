from django.contrib import admin

# Register your models here.

from.models import Band, Rhythm, Message, Music

admin.site.register(Band)
admin.site.register(Music)
admin.site.register(Rhythm)
admin.site.register(Message)

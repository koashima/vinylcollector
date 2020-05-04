from django.contrib import admin
from . models import Vinyl, Listening, Contributor

admin.site.register(Vinyl)
admin.site.register(Listening)
admin.site.register(Contributor)
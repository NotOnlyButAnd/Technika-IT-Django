from django.contrib import admin
from client_app.models import *

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    model = Image

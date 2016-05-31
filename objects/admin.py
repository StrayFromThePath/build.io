from django.contrib import admin
from .models import Objects, ObjectTypes, Properties, PropertiesTypes

admin.site.register(Objects)
admin.site.register(ObjectTypes)
admin.site.register(Properties)
admin.site.register(PropertiesTypes)

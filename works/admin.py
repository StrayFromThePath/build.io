from django.contrib import admin
from .models import Works, WorksTypes, WorksTypesMachinesTypes, Resourses, ResoursesTypes

admin.site.register(Works)
admin.site.register(WorksTypes)
admin.site.register(WorksTypesMachinesTypes)
admin.site.register(Resourses)
admin.site.register(ResoursesTypes)

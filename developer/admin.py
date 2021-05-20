from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Member)
admin.site.register(AllProfile)
admin.site.register(Test)
admin.site.register(Invitation)
admin.site.register(Skill)
admin.site.register(Response)

class SkillInline(admin.StackedInline):
    model=Skill



class AllProfileAdmin(admin.ModelAdmin):
    inlines = [
        SkillInline,
    ]

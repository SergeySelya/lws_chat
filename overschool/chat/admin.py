from django.contrib import admin
from .models import Message, Members, Groups


@admin.register(Message)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['username', 'room', 'content', 'date_added']


@admin.register(Groups)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['group_name', 'id']


@admin.register(Members)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'group_id']



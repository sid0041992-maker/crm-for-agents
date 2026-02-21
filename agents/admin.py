from django.contrib import admin
from .models import Agent

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'role', 'created_at')
    list_filter = ('role',)
    search_fields = ('name', 'phone')
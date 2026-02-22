from django.contrib import admin
from .models import User, Agent, Property, Deal

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'role', 'created_at')
    list_filter = ('role',)
    search_fields = ('name', 'phone')

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    search_fields = ('user__name', 'user__phone')

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('address', 'property_type', 'area', 'status', 'owner', 'agent')
    list_filter = ('property_type', 'status')
    search_fields = ('address',)

@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    list_display = ('id', 'agent', 'rent_amount', 'has_insurance', 'created_at')
    list_filter = ('has_insurance', 'created_at')
    search_fields = ('agent__user__name', 'agent__user__phone')
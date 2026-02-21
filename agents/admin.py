from django.contrib import admin
from .models import Agent, Deal

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'role', 'created_at')
    list_filter = ('role',)
    search_fields = ('name', 'phone')


@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'agent',
        'rent_amount',
        'has_insurance',
        'display_agent_commission',
        'display_our_commission',
        'display_total_commission',
        'created_at'
    )
    list_filter = ('has_insurance', 'created_at')
    search_fields = ('agent__name', 'agent__phone')

    def display_agent_commission(self, obj):
        return f"{obj.calculate_commission()['agent_commission']} ₽"
    display_agent_commission.short_description = "Комиссия агента"

    def display_our_commission(self, obj):
        return f"{obj.calculate_commission()['our_commission']} ₽"
    display_our_commission.short_description = "Наша комиссия"

    def display_total_commission(self, obj):
        return f"{obj.calculate_commission()['total']} ₽"
    display_total_commission.short_description = "Итого"
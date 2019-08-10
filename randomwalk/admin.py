from django.contrib import admin
from .models import SampleData, BlackScholes, BrownianMotion

# Register your models here.

class SampleDataAdmin(admin.ModelAdmin):
    list_display = ('created', 'direction', 'ip_address')

class BlackScholesAdmin(admin.ModelAdmin):
    list_display = ('created', 'price', 'strike', 'interest_rate', 'volatility', 'time_to_exp')

class BrownianMotionAdmin(admin.ModelAdmin):
    list_display = ('created', 'volatility', 'variance', 'start', 'count')

admin.site.register(SampleData, SampleDataAdmin)
admin.site.register(BlackScholes, BlackScholesAdmin)
admin.site.register(BrownianMotion, BrownianMotionAdmin)
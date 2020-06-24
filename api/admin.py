from django.contrib import admin
from .models import Metal, Rate


class MetalAdmin(admin.ModelAdmin):
    pass


class RateAdmin(admin.ModelAdmin):
    pass


admin.site.register(Metal, MetalAdmin)
admin.site.register(Rate, RateAdmin)
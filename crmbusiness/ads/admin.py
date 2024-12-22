from django.contrib import admin

from .models import PromotionChannel


class AdvertisingInline(admin.TabularInline):
    model = PromotionChannel.advertising.through
    extra = 0
    verbose_name = 'Рекламная кампания'
    verbose_name_plural = 'Рекламные кампании'

@admin.register(PromotionChannel)
class PromotionChannelAdmin(admin.ModelAdmin):
    inlines = [
        AdvertisingInline,
    ]
    list_display = 'custom_pk', 'name'
    list_display_links = 'custom_pk', 'name'
    ordering = 'pk',

    def custom_pk(self, obj: PromotionChannel):
        return obj.pk

    custom_pk.short_description = 'id'

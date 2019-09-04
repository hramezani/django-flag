from django.contrib import admin

from pinax.flag.models import FlaggedContent, FlagInstance


class InlineFlagInstance(admin.TabularInline):
    model = FlagInstance
    extra = 0


class FlaggedContentAdmin(admin.ModelAdmin):
    inlines = [InlineFlagInstance]


admin.site.register(FlaggedContent, FlaggedContentAdmin)

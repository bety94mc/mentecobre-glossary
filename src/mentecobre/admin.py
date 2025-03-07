from django.contrib import admin
from django.contrib.admin.models import DELETION
from django.urls import reverse
from django.utils.html import escape
from django.utils.safestring import mark_safe

from import_export.admin import ImportExportModelAdmin

from .models import Glossary
from django.contrib.admin.models import LogEntry


@admin.register(Glossary)
class GlossaryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'wordEn', 'wordEs', 'universe')
    list_filter = ['universe']
    search_fields = ('wordEn', 'wordEs')

@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    date_hierarchy = 'action_time'

    list_filter = [
        'user',
        'content_type',
        'action_flag'
    ]

    search_fields = [
        'object_repr',
        'change_message'
    ]

    list_display = [
        'action_time',
        'user',
        'content_type',
        'object_link',
        'action_flag',
    ]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser

    def object_link(self, obj):
        if obj.action_flag == DELETION:
            link = escape(obj.object_repr)
        else:
            ct = obj.content_type
            link = '<a href="%s">%s</a>' % (
                reverse('admin:%s_%s_change' % (ct.app_label, ct.model), args=[obj.object_id]),
                escape(obj.object_repr),
            )
        return mark_safe(link)
    object_link.admin_order_field = "object_repr"
    object_link.short_description = "object"



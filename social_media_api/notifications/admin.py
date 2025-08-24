from django.contrib import admin
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('recipient', 'actor', 'verb', 'read')
    list_filter = ('read', 'timestamp')
    search_fields = ('verb', 'recipient__username', 'actor__username')
    ordering = ('timestamp',)

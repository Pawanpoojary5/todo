from django.contrib import admin
from django.utils.html import format_html
from .models import Feature, Todo, SuggestedFeature


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    """Professional feature administration"""
    list_display = ('title', 'order', 'is_active_badge', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title', 'description')
    ordering = ('order',)
    fieldsets = (
        ('Feature Information', {
            'fields': ('title', 'description', 'icon_svg', 'order')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('created_at', 'updated_at')

    def is_active_badge(self, obj):
        """Display active status as colored badge"""
        if obj.is_active:
            return format_html(
                '<span style="background-color: #10b981; color: white; padding: 3px 10px; border-radius: 3px; font-size: 11px; font-weight: bold;">ACTIVE</span>'
            )
        return format_html(
            '<span style="background-color: #ef4444; color: white; padding: 3px 10px; border-radius: 3px; font-size: 11px; font-weight: bold;">INACTIVE</span>'
        )
    is_active_badge.short_description = 'Status'


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    """Professional todo administration"""
    list_display = ('title', 'user', 'priority_badge', 'status_badge', 'due_date', 'created_at')
    list_filter = ('status', 'priority', 'created_at', 'user')
    search_fields = ('title', 'description', 'user__username')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at', 'completed_at')
    fieldsets = (
        ('Task Information', {
            'fields': ('user', 'title', 'description')
        }),
        ('Task Status', {
            'fields': ('priority', 'status', 'due_date', 'completed_at')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def priority_badge(self, obj):
        """Display priority as colored badge"""
        colors = {
            'low': '#3b82f6',
            'medium': '#f59e0b',
            'high': '#ef4444',
            'urgent': '#991b1b',
        }
        return format_html(
            '<span style="background-color: {}; color: white; padding: 3px 10px; border-radius: 3px; font-size: 11px; font-weight: bold;">{}</span>',
            colors.get(obj.priority, '#6b7280'),
            obj.get_priority_display(),
        )
    priority_badge.short_description = 'Priority'

    def status_badge(self, obj):
        """Display status as colored badge"""
        colors = {
            'pending': '#9ca3af',
            'in_progress': '#3b82f6',
            'completed': '#10b981',
            'on_hold': '#ef4444',
        }
        return format_html(
            '<span style="background-color: {}; color: white; padding: 3px 10px; border-radius: 3px; font-size: 11px; font-weight: bold;">{}</span>',
            colors.get(obj.status, '#6b7280'),
            obj.get_status_display(),
        )
    status_badge.short_description = 'Status'


@admin.register(SuggestedFeature)
class SuggestedFeatureAdmin(admin.ModelAdmin):
    """Professional suggested feature administration"""
    list_display = ('title', 'user', 'votes', 'is_approved_badge', 'created_at')
    list_filter = ('is_approved', 'created_at', 'votes')
    search_fields = ('title', 'description', 'user__username')
    ordering = ('-votes', '-created_at')
    readonly_fields = ('created_at', 'updated_at', 'votes')
    fieldsets = (
        ('Feature Suggestion', {
            'fields': ('user', 'title', 'description')
        }),
        ('Approval Status', {
            'fields': ('is_approved', 'votes')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def is_approved_badge(self, obj):
        """Display approval status as colored badge"""
        if obj.is_approved:
            return format_html(
                '<span style="background-color: #10b981; color: white; padding: 3px 10px; border-radius: 3px; font-size: 11px; font-weight: bold;">✓ APPROVED</span>'
            )
        return format_html(
            '<span style="background-color: #f59e0b; color: white; padding: 3px 10px; border-radius: 3px; font-size: 11px; font-weight: bold;">⏳ PENDING</span>'
        )
    is_approved_badge.short_description = 'Status'

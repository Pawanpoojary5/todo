from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Feature(models.Model):
    """
    Professional feature model for showcasing application capabilities
    """
    title = models.CharField(max_length=100, help_text="Feature title")
    description = models.TextField(help_text="Detailed feature description")
    icon_svg = models.TextField(blank=True, null=True, help_text="SVG icon or icon name")
    order = models.IntegerField(default=0, help_text="Display order")
    is_active = models.BooleanField(default=True, help_text="Show/hide feature")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'Feature'
        verbose_name_plural = 'Features'

    def __str__(self):
        return self.title


class Todo(models.Model):
    """
    Professional Todo model with user ownership and priority management
    """
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('urgent', 'Urgent'),
    ]
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('on_hold', 'On Hold'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')
    title = models.CharField(max_length=200, help_text="Task title")
    description = models.TextField(blank=True, null=True, help_text="Task description")
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='medium',
        help_text="Task priority level"
    )
    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default='pending',
        help_text="Task status"
    )
    due_date = models.DateTimeField(blank=True, null=True, help_text="Due date")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['-priority', 'created_at']
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'
        indexes = [
            models.Index(fields=['user', '-created_at']),
            models.Index(fields=['status']),
        ]

    def __str__(self):
        return f"{self.title} ({self.get_status_display()})"

    def mark_completed(self):
        """Mark todo as completed"""
        self.status = 'completed'
        self.completed_at = timezone.now()
        self.save()


class SuggestedFeature(models.Model):
    """
    User-suggested features for future development
    """
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    votes = models.IntegerField(default=1)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-votes', '-created_at']
        verbose_name = 'Suggested Feature'
        verbose_name_plural = 'Suggested Features'

    def __str__(self):
        return f"{self.title} ({self.votes} votes)"

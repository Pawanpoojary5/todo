from django.db import models

class Feature(models.Model):
    # Title of the feature card
    title = models.CharField(max_length=100)

    # Small description shown under the title
    description = models.TextField()

    # The icon SVG or any icon name (optional)
    # If you want to store the SVG path, you can use TextField
    icon_svg = models.TextField(blank=True, null=True)

    # This field is optional but helps keep things in order
    order = models.IntegerField(default=0)

    def __str__(self):
        # Shows the feature name in admin panel
        return self.title

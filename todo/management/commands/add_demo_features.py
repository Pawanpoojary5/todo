from django.core.management.base import BaseCommand
from todo.models import Feature


class Command(BaseCommand):
    help = 'Add demo features to the database'

    def handle(self, *args, **options):
        features_data = [
            {
                'title': 'Lightning Fast',
                'description': 'Experience blazing-fast performance with optimized algorithms and efficient data structures.',
                'icon_svg': '⚡',
                'order': 0,
            },
            {
                'title': 'Smart Prioritization',
                'description': 'AI-powered task prioritization that learns from your work patterns and suggests optimal task ordering.',
                'icon_svg': '🎯',
                'order': 1,
            },
            {
                'title': 'Fully Responsive',
                'description': 'Works seamlessly across all devices - desktop, tablet, and mobile with adaptive interfaces.',
                'icon_svg': '📱',
                'order': 2,
            },
            {
                'title': 'Secure & Private',
                'description': 'Enterprise-grade security with end-to-end encryption ensuring your data remains private and safe.',
                'icon_svg': '🔒',
                'order': 3,
            },
            {
                'title': 'Dark Mode',
                'description': 'Easy on the eyes with a professionally designed dark mode for comfortable late-night productivity.',
                'icon_svg': '🌙',
                'order': 4,
            },
            {
                'title': 'Beautiful Design',
                'description': 'Stunning UI with smooth animations and intuitive interactions creating an enjoyable user experience.',
                'icon_svg': '✨',
                'order': 5,
            },
        ]

        created_count = 0
        for feature_data in features_data:
            feature, created = Feature.objects.get_or_create(
                title=feature_data['title'],
                defaults={
                    'description': feature_data['description'],
                    'icon_svg': feature_data['icon_svg'],
                    'order': feature_data['order'],
                    'is_active': True,
                }
            )
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'✓ Created feature: {feature.title}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'⚠ Feature already exists: {feature.title}')
                )

        self.stdout.write(
            self.style.SUCCESS(f'\n✓ Successfully added {created_count} new features!')
        )

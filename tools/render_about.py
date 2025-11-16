import os
import sys

# Ensure the project root is on sys.path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyTodo.settings')
import django
from django.template.loader import render_to_string

try:
    django.setup()
    output = render_to_string('about.html', {})
    print('TEMPLATE RENDERED SUCCESSFULLY')
    print(output[:1000])
except Exception as e:
    import traceback
    traceback.print_exc()
    sys.exit(1)

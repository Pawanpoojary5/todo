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
    # Provide an empty features context
    output = render_to_string('features.html', {'features': []})
    print('TEMPLATE RENDERED SUCCESSFULLY')
    print(output[:1000])
except Exception:
    import traceback
    traceback.print_exc()
    sys.exit(1)

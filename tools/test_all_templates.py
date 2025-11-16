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
    print("=" * 60)
    print("TESTING TEMPLATE RENDERING")
    print("=" * 60)
    
    # Test todowork
    print("\n1. Rendering todowork.html...")
    output = render_to_string('todowork.html', {})
    print("✓ todowork.html rendered successfully")
    
    # Test about
    print("\n2. Rendering about.html...")
    output = render_to_string('about.html', {})
    print("✓ about.html rendered successfully")
    
    # Test features
    print("\n3. Rendering features.html...")
    output = render_to_string('features.html', {'features': []})
    print("✓ features.html rendered successfully")
    
    print("\n" + "=" * 60)
    print("ALL TEMPLATES RENDERED SUCCESSFULLY! ✓")
    print("=" * 60)
    
except Exception as e:
    import traceback
    print("ERROR:")
    traceback.print_exc()
    sys.exit(1)

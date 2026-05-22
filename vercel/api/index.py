import os
import sys
from pathlib import Path

# Add parent directory to Python path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'spurs_site.settings')

# Import and get WSGI application
from django.core.wsgi import get_wsgi_application
app = get_wsgi_application()

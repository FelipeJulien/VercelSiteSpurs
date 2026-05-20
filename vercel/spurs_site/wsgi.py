"""
WSGI config for spurs_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os
import sys
from pathlib import Path

# Adiciona a raiz do projeto ao sys.path para o Vercel encontrar o módulo spurs_site
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'spurs_site.settings')

application = get_wsgi_application()

app = application

# Import os and Django functions and settings
import os
from django.core.wsgi import get_wsgi_application

# Specify the settings file
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogging_platform.settings')

# Get the application
application = get_wsgi_application()
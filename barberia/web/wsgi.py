import os  
import sys 
 
from django.core.wsgi import get_wsgi_application 
 
sys.path.append('/var/www/html/barberia/barberia') 
# adjust the Python version in the line below as needed 
sys.path.append('/var/www/html/barberia/env/lib/python3.5/site-packages') 
 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web.settings.prod") 
  
application = get_wsgi_application() 
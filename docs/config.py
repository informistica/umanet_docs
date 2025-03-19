import os
import sys
import django

# Percorso del progetto Django (deve essere regolato in base alla tua struttura)
DJANGO_PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../educa"))

sys.path.insert(0, DJANGO_PROJECT_PATH)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "educa.settings")

django.setup()

# créditos: http://engineroom.trackmaven.com/blog/using-pytest-with-django/
import os
import django
from django.conf import settings

# variável de ambiente para definir quais configurações serão utilizadas
# trocar lms.setting pelo nome do pacote do seu app
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lms.settings')


# `pytest` chama automaticamente esta função quando testes são executados.
def pytest_configure():
    settings.DEBUG = False    
    django.setup()
    
################ LightWeight Django #################
##################-- settings --#####################
import os
import sys

from django.conf import settings

# DEBUG = os.environ.get('DEBUG', 'on') == 'on'
# SECRET_KEY = os.environ.get('SECRET_KEY', '(y9onxs*(49r&e+!7$spye!ua6d9!_=z7i82ftr=20bk5o0rcd') #os.urandom(32))
# ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')

BASE_DIR = os.path.dirname(__file__)

settings.configure(
	DEBUG = True,
	SECRET_KEY = '(y9onxs*(49r&e+!7$spye!ua6d9!_=z7i82ftr=20bk5o0rcd',
	ROOT_URLCONF = 'sitebuilder.urls',
	MIDDLEWARE_CLASSES = (
		# 'django.middleware.common.CommonMiddleware',
		# 'django.middleware.csrf.CsrfViewMiddleware',
		# 'django.middleware.clickjacking.XFrameOptionsMiddleware',
	),
	INSTALLED_APPS = (
		'django.contrib.staticfiles',
		'sitebuilder',
	),
	TEMPLATES = (
		{
			'BACKEND': 'django.template.backends.django.DjangoTemplates',
			'DIRS': [],
			'APP_DIRS': True,
		},
	),
	STATIC_URL = '/static/',
	SITE_PAGES_DIRECTORY = os.path.join(BASE_DIR, 'pages'),
	SITE_OUTPUT_DIRECTORY = os.path.join(BASE_DIR, '_build'),
	STATIC_ROOT = os.path.join(BASE_DIR, '_build', 'static'),
)
##################-- settings --#####################

##################-- manage --#####################
if __name__ == '__main__':
	from django.core.management import execute_from_command_line

	execute_from_command_line(sys.argv)
##################-- manage --#####################

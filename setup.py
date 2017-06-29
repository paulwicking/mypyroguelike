try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'Spork',
	'author': 'wowsuchnamaste',
	'url': 'URL to get it at',
	'download_url': 'where to download it',
	'author_email': 'my email',
	'version': '0.1'
	'install_requires': ['nose'],
	'packages': ['spork'],
	'scripts': [],
	'name': 'spork'
}

setup(**config)


from django.conf import settings
from genericpath import exists
from os.path import join
from re import match


class Theme:
	"""
	See the :doc:`documentation <layout>` for the structure of themes.
	"""
	def __init__(self, name):
		assert match(r'^[a-zA-Z][a-zA-Z0-9\.\-,_]+$', name), \
			'Theme names should contain only letters, numbers and "_-+,." (got "{0:s}")'.format(name)
		self.base_template = join(settings.SV_THEMES_DIR, 'templates', name, 'base.html')
		assert exists(self.base_template), 'theme {0:s}: can\'t find "{1:s}"'.format(name, self.base_template)
		self.readme = self.description = self.credits = self.license = None
		self.name = name
		self.load()

	def load(self):
		self.load_info()

	def load_info(self):
		info_files = ('readme.rst', 'description.rst', 'credits.rst', 'license.txt')
		info_path = join(settings.SV_THEMES_DIR, 'info', self.name)
		for info_file in info_files:
			attr_name = info_file.rsplit('.', maxsplit=1)[0]
			setattr(self, attr_name, None)
			if exists(join(info_path, info_file)):
				with open(join(info_path, info_file), 'r') as fh:
					setattr(self, attr_name, fh.read())

	def prefix(self):
		return self.name

	def relative_template_head_path(self):
		if exists(join(settings.SV_THEMES_DIR, 'templates', self.name, 'head.html')):
			return '{0:s}/{1:s}'.format(self.name, 'head.html')
		return 'default_head.html'

	def relative_template_path(self):
		return '{0:s}/{1:s}'.format(self.name, 'base.html')

	def disp_name(self):
		return self.name.title()



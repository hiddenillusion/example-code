import os
import sys

current_dir = os.path.abspath(os.path.dirname(__file__))
root_dir = os.path.normpath(os.path.join(current_dir, ".."))        
sys.path.insert(0,root_dir) 

from PluginManager import PluginInterface
from PluginManager import Manager

class PluginOne(PluginInterface):
	name = "Plugin1"

	def standard_view(self):
		standard_row = {}
		standard_row['last_write_time'] = ''

		return standard_row

	def show_details(self):
		plugin_details = {}
		plugin_details['artifact_type'] = "reg"
		plugin_details['author'] = "Glenn Edwards"
		plugin_details['categories'] = ['program_execution', 'user_activity']
		plugin_details['date'] = "2015-04-09"	
		plugin_details['description'] = "my test plugin #1"
		plugin_details['fields'] = ','.join(field for field, value in self.standard_view().iteritems())
		plugin_details['name'] = self.name
		plugin_details['path'] = ('' if __file__ is None else os.path.abspath(__file__))
		plugin_details['references'] = ""
		plugin_details['requirements'] = "ntuser.dat"
		plugin_details['version'] = "0.01"

		return plugin_details

	def process_plugin(self):
		print "processing man"

Manager().register_plugin(PluginOne)				
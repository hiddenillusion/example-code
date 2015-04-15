
""" Lists the details of available plugins """
import PluginManager
main_plugin_directory = "plugins"

plugins = PluginManager.Manager().get_all_plugins(main_plugin_directory)
for plugin_name, plugin_directory in plugins.iteritems():
	if plugin_name:
		found_plugin = PluginManager.Manager().find_plugin(plugin_name, plugin_directory)
		if found_plugin:
			activated_plugin = PluginManager.Manager().load_plugin(plugin_name, found_plugin)

for plugin_name, plugin_class in PluginManager.PluginInterface().registry.iteritems():
	try:
		PluginManager.Manager().show_cls_details(plugin_class)
	# something's wrong at this point
	except AttributeError as err:
		pass
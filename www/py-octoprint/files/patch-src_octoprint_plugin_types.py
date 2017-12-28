--- src/octoprint/plugin/types.py.orig	2017-12-12 11:42:40 UTC
+++ src/octoprint/plugin/types.py
@@ -1481,7 +1481,7 @@ class SettingsPlugin(OctoPrintPlugin):
 
 		:return: the current settings of the plugin, as a dictionary
 		"""
-		from flask.ext.login import current_user
+		from flask_login import current_user
 		import copy
 
 		data = copy.deepcopy(self._settings.get_all_data(merged=True))

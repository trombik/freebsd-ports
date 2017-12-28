--- src/octoprint/plugin/types.py.orig	2017-12-12 11:42:40 UTC
+++ src/octoprint/plugin/types.py
@@ -1481,7 +1481,7 @@ class SettingsPlugin(OctoPrintPlugin):
 
 		:return: the current settings of the plugin, as a dictionary
 		"""
-		from flask.ext.login import current_user
+		from flask_login import current_user
 		import copy
 
 		data = copy.deepcopy(self._settings.get_all_data(merged=True))
@@ -1527,8 +1527,8 @@ class SettingsPlugin(OctoPrintPlugin):
 					else:
 						node[key] = None
 
-		conditions = dict(user=lambda: current_user is not None and not current_user.is_anonymous(),
-		                  admin=lambda: current_user is not None and not current_user.is_anonymous() and current_user.is_admin(),
+		conditions = dict(user=lambda: current_user is not None and not current_user.is_anonymous,
+		                  admin=lambda: current_user is not None and not current_user.is_anonymous and current_user.is_admin,
 		                  never=lambda: False)
 
 		for level, condition in conditions.items():

--- src/octoprint/server/api/settings.py.orig	2017-12-12 11:42:40 UTC
+++ src/octoprint/server/api/settings.py
@@ -8,7 +8,7 @@ __copyright__ = "Copyright (C) 2014 The OctoPrint Proj
 import logging
 
 from flask import request, jsonify, make_response
-from flask.ext.login import current_user
+from flask_login import current_user
 from werkzeug.exceptions import BadRequest
 
 from octoprint.events import eventManager, Events
@@ -39,7 +39,7 @@ def _etag(lm=None):
 	for key in sorted(plugin_settings.keys()):
 		sorted_plugin_settings[key] = plugin_settings.get(key, dict())
 
-	if current_user is not None and not current_user.is_anonymous():
+	if current_user is not None and not current_user.is_anonymous:
 		roles = sorted(current_user.roles)
 	else:
 		roles = []

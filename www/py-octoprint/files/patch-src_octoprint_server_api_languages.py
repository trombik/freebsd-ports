--- src/octoprint/server/api/languages.py.orig	2017-12-12 11:42:40 UTC
+++ src/octoprint/server/api/languages.py
@@ -26,7 +26,7 @@ from octoprint.server.util.flask import restricted_acc
 
 from octoprint.plugin import plugin_manager
 
-from flask.ext.babel import Locale
+from flask_babel import Locale
 
 @api.route("/languages", methods=["GET"])
 @restricted_access

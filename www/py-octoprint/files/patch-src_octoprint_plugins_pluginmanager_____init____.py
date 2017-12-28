--- src/octoprint/plugins/pluginmanager/__init__.py.orig	2017-12-28 07:58:33 UTC
+++ src/octoprint/plugins/pluginmanager/__init__.py
@@ -18,7 +18,7 @@ from octoprint.util.version import get_octoprint_versi
 from octoprint.util.platform import get_os
 
 from flask import jsonify, make_response
-from flask.ext.babel import gettext
+from flask_babel import gettext
 
 import logging
 import sarge

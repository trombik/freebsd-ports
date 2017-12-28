--- src/octoprint/server/api/system.py.orig	2017-12-28 07:58:33 UTC
+++ src/octoprint/server/api/system.py
@@ -10,7 +10,7 @@ import sarge
 import threading
 
 from flask import request, make_response, jsonify, url_for
-from flask.ext.babel import gettext
+from flask_babel import gettext
 
 from octoprint.settings import settings as s
 

--- src/octoprint/server/api/settings.py.orig	2017-12-28 07:58:33 UTC
+++ src/octoprint/server/api/settings.py
@@ -8,7 +8,7 @@ __copyright__ = "Copyright (C) 2014 The OctoPrint Proj
 import logging
 
 from flask import request, jsonify, make_response
-from flask.ext.login import current_user
+from flask_login import current_user
 from werkzeug.exceptions import BadRequest
 
 from octoprint.events import eventManager, Events

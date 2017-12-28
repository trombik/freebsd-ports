--- src/octoprint/server/api/users.py.orig	2017-12-12 11:42:40 UTC
+++ src/octoprint/server/api/users.py
@@ -7,7 +7,7 @@ __copyright__ = "Copyright (C) 2014 The OctoPrint Proj
 
 from flask import request, jsonify, abort, make_response
 from werkzeug.exceptions import BadRequest
-from flask.ext.login import current_user
+from flask_login import current_user
 
 import octoprint.users as users
 

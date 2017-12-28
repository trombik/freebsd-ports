--- src/octoprint/server/api/users.py.orig	2017-12-12 11:42:40 UTC
+++ src/octoprint/server/api/users.py
@@ -7,7 +7,7 @@ __copyright__ = "Copyright (C) 2014 The OctoPrint Proj
 
 from flask import request, jsonify, abort, make_response
 from werkzeug.exceptions import BadRequest
-from flask.ext.login import current_user
+from flask_login import current_user
 
 import octoprint.users as users
 
@@ -72,7 +72,7 @@ def getUser(username):
 	if not userManager.enabled:
 		return jsonify(SUCCESS)
 
-	if current_user is not None and not current_user.is_anonymous() and (current_user.get_name() == username or current_user.is_admin()):
+	if current_user is not None and not current_user.is_anonymous and (current_user.get_name() == username or current_user.is_admin):
 		user = userManager.findUser(username)
 		if user is not None:
 			return jsonify(user.asDict())
@@ -133,7 +133,7 @@ def changePasswordForUser(username):
 	if not userManager.enabled:
 		return jsonify(SUCCESS)
 
-	if current_user is not None and not current_user.is_anonymous() and (current_user.get_name() == username or current_user.is_admin()):
+	if current_user is not None and not current_user.is_anonymous and (current_user.get_name() == username or current_user.is_admin):
 		if not "application/json" in request.headers["Content-Type"]:
 			return make_response("Expected content-type JSON", 400)
 
@@ -161,7 +161,7 @@ def getSettingsForUser(username):
 	if not userManager.enabled:
 		return jsonify(SUCCESS)
 
-	if current_user is None or current_user.is_anonymous() or (current_user.get_name() != username and not current_user.is_admin()):
+	if current_user is None or current_user.is_anonymous or (current_user.get_name() != username and not current_user.is_admin):
 		return make_response("Forbidden", 403)
 
 	try:
@@ -175,7 +175,7 @@ def changeSettingsForUser(username):
 	if not userManager.enabled:
 		return jsonify(SUCCESS)
 
-	if current_user is None or current_user.is_anonymous() or (current_user.get_name() != username and not current_user.is_admin()):
+	if current_user is None or current_user.is_anonymous or (current_user.get_name() != username and not current_user.is_admin):
 		return make_response("Forbidden", 403)
 
 	try:
@@ -195,7 +195,7 @@ def deleteApikeyForUser(username):
 	if not userManager.enabled:
 		return jsonify(SUCCESS)
 
-	if current_user is not None and not current_user.is_anonymous() and (current_user.get_name() == username or current_user.is_admin()):
+	if current_user is not None and not current_user.is_anonymous and (current_user.get_name() == username or current_user.is_admin):
 		try:
 			userManager.deleteApikey(username)
 		except users.UnknownUser:
@@ -211,7 +211,7 @@ def generateApikeyForUser(username):
 	if not userManager.enabled:
 		return jsonify(SUCCESS)
 
-	if current_user is not None and not current_user.is_anonymous() and (current_user.get_name() == username or current_user.is_admin()):
+	if current_user is not None and not current_user.is_anonymous and (current_user.get_name() == username or current_user.is_admin):
 		try:
 			apikey = userManager.generateApiKey(username)
 		except users.UnknownUser:

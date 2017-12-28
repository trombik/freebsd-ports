--- src/octoprint/server/api/__init__.py.orig	2017-12-12 11:42:40 UTC
+++ src/octoprint/server/api/__init__.py
@@ -10,8 +10,8 @@ import netaddr
 import sarge
 
 from flask import Blueprint, request, jsonify, abort, current_app, session, make_response, g
-from flask.ext.login import login_user, logout_user, current_user
-from flask.ext.principal import Identity, identity_changed, AnonymousIdentity
+from flask_login import login_user, logout_user, current_user
+from flask_principal import Identity, identity_changed, AnonymousIdentity
 
 import octoprint.util as util
 import octoprint.users
@@ -62,7 +62,7 @@ def pluginData(name):
 		return make_response("More than one api provider registered for {name}, can't proceed".format(name=name), 500)
 
 	api_plugin = api_plugins[0]
-	if api_plugin.is_api_adminonly() and not current_user.is_admin():
+	if api_plugin.is_api_adminonly() and not current_user.is_admin:
 		return make_response("Forbidden", 403)
 
 	response = api_plugin.on_api_get(request)
@@ -89,7 +89,7 @@ def pluginCommand(name):
 	if valid_commands is None:
 		return make_response("Method not allowed", 405)
 
-	if api_plugin.is_api_adminonly() and not current_user.is_admin():
+	if api_plugin.is_api_adminonly() and not current_user.is_admin:
 		return make_response("Forbidden", 403)
 
 	command, data, response = get_json_command_from_request(request, valid_commands)

--- src/octoprint/server/api/__init__.py.orig	2017-12-28 07:58:33 UTC
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

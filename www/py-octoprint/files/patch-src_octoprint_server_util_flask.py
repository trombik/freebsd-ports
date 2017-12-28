--- src/octoprint/server/util/flask.py.orig	2017-12-12 11:42:40 UTC
+++ src/octoprint/server/util/flask.py
@@ -8,9 +8,9 @@ __copyright__ = "Copyright (C) 2014 The OctoPrint Proj
 
 import tornado.web
 import flask
-import flask.ext.login
-import flask.ext.principal
-import flask.ext.assets
+import flask_login
+import flask_principal
+import flask_assets
 import webassets.updater
 import webassets.utils
 import functools
@@ -45,7 +45,7 @@ def enable_additional_translations(default_locale="en"
 	import os
 	from flask import _request_ctx_stack
 	from babel import support, Locale
-	import flask.ext.babel
+	import flask_babel
 
 	if additional_folders is None:
 		additional_folders = []
@@ -96,7 +96,7 @@ def enable_additional_translations(default_locale="en"
 			return None
 		translations = getattr(ctx, 'babel_translations', None)
 		if translations is None:
-			locale = flask.ext.babel.get_locale()
+			locale = flask_babel.get_locale()
 			translations = support.Translations()
 
 			if str(locale) != default_locale:
@@ -134,8 +134,8 @@ def enable_additional_translations(default_locale="en"
 			ctx.babel_translations = translations
 		return translations
 
-	flask.ext.babel.Babel.list_translations = fixed_list_translations
-	flask.ext.babel.get_translations = fixed_get_translations
+	flask_babel.Babel.list_translations = fixed_list_translations
+	flask_babel.get_translations = fixed_get_translations
 
 def fix_webassets_cache():
 	from webassets import cache
@@ -486,12 +486,12 @@ class OctoPrintFlaskResponse(flask.Response):
 
 def passive_login():
 	if octoprint.server.userManager.enabled:
-		user = octoprint.server.userManager.login_user(flask.ext.login.current_user)
+		user = octoprint.server.userManager.login_user(flask_login.current_user)
 	else:
-		user = flask.ext.login.current_user
+		user = flask_login.current_user
 
 	if user is not None and not user.is_anonymous() and user.is_active():
-		flask.ext.principal.identity_changed.send(flask.current_app._get_current_object(), identity=flask.ext.principal.Identity(user.get_id()))
+		flask_principal.identity_changed.send(flask.current_app._get_current_object(), identity=flask_principal.Identity(user.get_id()))
 		if hasattr(user, "session"):
 			flask.session["usersession.id"] = user.session
 		flask.g.user = user
@@ -513,8 +513,8 @@ def passive_login():
 					user = octoprint.server.userManager.login_user(user)
 					flask.session["usersession.id"] = user.session
 					flask.g.user = user
-					flask.ext.login.login_user(user)
-					flask.ext.principal.identity_changed.send(flask.current_app._get_current_object(), identity=flask.ext.principal.Identity(user.get_id()))
+					flask_login.login_user(user)
+					flask_principal.identity_changed.send(flask.current_app._get_current_object(), identity=flask_principal.Identity(user.get_id()))
 					return flask.jsonify(user.asDict())
 		except:
 			logger = logging.getLogger(__name__)
@@ -1059,14 +1059,14 @@ def _get_flask_user_from_request(request):
 	:return: the user or None if no user could be determined
 	"""
 	import octoprint.server.util
-	import flask.ext.login
+	import flask_login
 	from octoprint.settings import settings
 
 	apikey = octoprint.server.util.get_api_key(request)
 	if settings().getBoolean(["api", "enabled"]) and apikey is not None:
 		user = octoprint.server.util.get_user_for_apikey(apikey)
 	else:
-		user = flask.ext.login.current_user
+		user = flask_login.current_user
 
 	return user
 
@@ -1111,7 +1111,7 @@ def restricted_access(func):
 		if settings().getBoolean(["server", "firstRun"]) and settings().getBoolean(["accessControl", "enabled"]) and (octoprint.server.userManager is None or not octoprint.server.userManager.hasBeenCustomized()):
 			return flask.make_response("OctoPrint isn't setup yet", 403)
 
-		return flask.ext.login.login_required(func)(*args, **kwargs)
+		return flask_login.login_required(func)(*args, **kwargs)
 
 	return decorated_view
 
@@ -1229,7 +1229,7 @@ def get_json_command_from_request(request, valid_comma
 
 ##~~ Flask-Assets resolver with plugin asset support
 
-class PluginAssetResolver(flask.ext.assets.FlaskResolver):
+class PluginAssetResolver(flask_assets.FlaskResolver):
 
 	def split_prefix(self, ctx, item):
 		app = ctx.environment._app
@@ -1238,14 +1238,14 @@ class PluginAssetResolver(flask.ext.assets.FlaskResolv
 				prefix, plugin, name = item.split("/", 2)
 				blueprint = prefix + "." + plugin
 
-				directory = flask.ext.assets.get_static_folder(app.blueprints[blueprint])
+				directory = flask_assets.get_static_folder(app.blueprints[blueprint])
 				item = name
 				endpoint = blueprint + ".static"
 				return directory, item, endpoint
 			except (ValueError, KeyError):
 				pass
 
-		return flask.ext.assets.FlaskResolver.split_prefix(self, ctx, item)
+		return flask_assets.FlaskResolver.split_prefix(self, ctx, item)
 
 	def resolve_output_to_path(self, ctx, target, bundle):
 		import os

--- src/octoprint/server/util/__init__.py.orig	2017-12-12 11:42:40 UTC
+++ src/octoprint/server/util/__init__.py
@@ -68,9 +68,9 @@ def loginFromApiKeyRequestHandler():
 		return
 	
 	user = get_user_for_apikey(apikey)
-	if user is not None and _flask.ext.login.login_user(user, remember=False):
-		_flask.ext.principal.identity_changed.send(_flask.current_app._get_current_object(),
-		                                           identity=_flask.ext.principal.Identity(user.get_id()))
+	if user is not None and _flask_login.login_user(user, remember=False):
+		_flask_principal.identity_changed.send(_flask.current_app._get_current_object(),
+		                                           identity=_flask_principal.Identity(user.get_id()))
 	else:
 		return _flask.make_response("Invalid API key", 401)
 

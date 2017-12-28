--- src/octoprint/server/__init__.py.orig	2017-12-12 11:42:40 UTC
+++ src/octoprint/server/__init__.py
@@ -562,7 +562,7 @@ class Server(object):
 
 		self._tornado_app = Application(handlers=server_routes,
 		                                transforms=transforms)
-		max_body_sizes = [
+		max_body_size = [
 			("POST", r"/api/files/([^/]*)", self._settings.getInt(["server", "uploads", "maxSize"])),
 			("POST", r"/api/languages", 5 * 1024 * 1024)
 		]
@@ -570,7 +570,7 @@ class Server(object):
 		# allow plugins to extend allowed maximum body sizes
 		for name, hook in pluginManager.get_hooks("octoprint.server.http.bodysize").items():
 			try:
-				result = hook(list(max_body_sizes))
+				result = hook(list(max_body_size))
 			except:
 				self._logger.exception("There was an error while retrieving additional upload sizes from plugin hook {name}".format(**locals()))
 			else:
@@ -587,12 +587,12 @@ class Server(object):
 						route = r"/plugin/{name}/{route}".format(name=name, route=route if not route.startswith("/") else route[1:])
 
 						self._logger.debug("Adding maximum body size of {size}B for {method} requests to {route})".format(**locals()))
-						max_body_sizes.append((method, route, size))
+						max_body_size.append((method, route, size))
 
 		self._stop_intermediary_server()
 
 		# initialize and bind the server
-		self._server = util.tornado.CustomHTTPServer(self._tornado_app, max_body_sizes=max_body_sizes, default_max_body_size=self._settings.getInt(["server", "maxSize"]))
+		self._server = util.tornado.CustomHTTPServer(self._tornado_app, max_body_size=max_body_size)
 		self._server.listen(self._port, address=self._host)
 
 		### From now on it's ok to launch subprocesses again

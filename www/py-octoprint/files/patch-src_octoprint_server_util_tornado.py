--- src/octoprint/server/util/tornado.py.orig	2017-12-12 11:42:40 UTC
+++ src/octoprint/server/util/tornado.py
@@ -718,7 +718,7 @@ class CustomHTTPServer(tornado.httpserver.HTTPServer):
 				 decompress_request=False,
 				 chunk_size=None, max_header_size=None,
 				 idle_connection_timeout=None, body_timeout=None,
-				 max_body_sizes=None, default_max_body_size=None, max_buffer_size=None):
+				 max_body_size=None, default_max_body_size=None, max_buffer_size=None):
 		self.request_callback = request_callback
 		self.no_keep_alive = no_keep_alive
 		self.xheaders = xheaders
@@ -728,7 +728,7 @@ class CustomHTTPServer(tornado.httpserver.HTTPServer):
 			chunk_size=chunk_size,
 			max_header_size=max_header_size,
 			header_timeout=idle_connection_timeout or 3600,
-			max_body_sizes=max_body_sizes,
+			max_body_size=max_body_size,
 			default_max_body_size=default_max_body_size,
 			body_timeout=body_timeout)
 		tornado.tcpserver.TCPServer.__init__(self, io_loop=io_loop, ssl_options=ssl_options,
@@ -790,7 +790,7 @@ class CustomHTTP1Connection(tornado.http1connection.HT
 		tornado.http1connection.HTTP1Connection.__init__(self, stream, is_client, params=params, context=context)
 
 		import re
-		self._max_body_sizes = map(lambda x: (x[0], re.compile(x[1]), x[2]), self.params.max_body_sizes or list())
+		self._max_body_size = map(lambda x: (x[0], re.compile(x[1]), x[2]), self.params.max_body_size or list())
 		self._default_max_body_size = self.params.default_max_body_size or self.stream.max_buffer_size
 
 	def _read_body(self, code, headers, delegate):
@@ -853,7 +853,7 @@ class CustomHTTP1Connection(tornado.http1connection.HT
 		         length
 		"""
 
-		for m, p, s in self._max_body_sizes:
+		for m, p, s in self._max_body_size:
 			if method == m and p.match(path):
 				return s
 		return self._default_max_body_size
@@ -869,7 +869,7 @@ class CustomHTTP1ConnectionParameters(tornado.http1con
 
 	def __init__(self, *args, **kwargs):
 		tornado.http1connection.HTTP1ConnectionParameters.__init__(self, args, kwargs)
-		self.max_body_sizes = kwargs["max_body_sizes"] if "max_body_sizes" in kwargs else list()
+		self.max_body_size = kwargs["max_body_size"] if "max_body_size" in kwargs else list()
 		self.default_max_body_size = kwargs["default_max_body_size"] if "default_max_body_size" in kwargs else None
 
 #~~ customized large response handler

--- src/octoprint/plugins/discovery/__init__.py.orig	2017-12-28 07:58:33 UTC
+++ src/octoprint/plugins/discovery/__init__.py
@@ -11,7 +11,7 @@ The SSDP/UPNP implementations has been largely inspire
 
 import logging
 import flask
-from flask.ext.babel import gettext
+from flask_babel import gettext
 
 # noinspection PyCompatibility
 from builtins import range

--- src/octoprint/plugins/octopi_support/__init__.py.orig	2017-12-28 07:58:33 UTC
+++ src/octoprint/plugins/octopi_support/__init__.py
@@ -7,7 +7,7 @@ __copyright__ = "Copyright (C) 2017 The OctoPrint Proj
 import flask
 import os
 
-from flask.ext.babel import gettext
+from flask_babel import gettext
 
 import octoprint.plugin
 

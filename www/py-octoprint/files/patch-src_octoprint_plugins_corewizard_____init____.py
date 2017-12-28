--- src/octoprint/plugins/corewizard/__init__.py.orig	2017-12-28 07:58:33 UTC
+++ src/octoprint/plugins/corewizard/__init__.py
@@ -6,7 +6,7 @@ __copyright__ = "Copyright (C) 2015 The OctoPrint Proj
 
 import octoprint.plugin
 
-from flask.ext.babel import gettext
+from flask_babel import gettext
 from .subwizards import Subwizards
 
 

--- src/octoprint/plugins/corewizard/subwizards.py.orig	2017-12-28 07:58:33 UTC
+++ src/octoprint/plugins/corewizard/subwizards.py
@@ -8,7 +8,7 @@ import octoprint.plugin
 
 import sys
 import inspect
-from flask.ext.babel import gettext
+from flask_babel import gettext
 
 
 # noinspection PyUnresolvedReferences,PyMethodMayBeStatic

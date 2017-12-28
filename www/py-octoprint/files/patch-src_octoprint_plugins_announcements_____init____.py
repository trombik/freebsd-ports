--- src/octoprint/plugins/announcements/__init__.py.orig	2017-12-28 07:58:33 UTC
+++ src/octoprint/plugins/announcements/__init__.py
@@ -23,7 +23,7 @@ from collections import OrderedDict
 from octoprint.server import admin_permission
 from octoprint.server.util.flask import restricted_access, with_revalidation_checking, check_etag
 from octoprint.util import utmify
-from flask.ext.babel import gettext
+from flask_babel import gettext
 from octoprint import __version__ as OCTOPRINT_VERSION
 
 class AnnouncementPlugin(octoprint.plugin.AssetPlugin,

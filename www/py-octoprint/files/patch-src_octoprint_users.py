--- src/octoprint/users.py.orig	2017-12-28 07:58:33 UTC
+++ src/octoprint/users.py
@@ -5,8 +5,8 @@ __author__ = "Gina Häußge <osd@foosel.net>"
 __license__ = 'GNU Affero General Public License http://www.gnu.org/licenses/agpl.html'
 __copyright__ = "Copyright (C) 2014 The OctoPrint Project - Released under terms of the AGPLv3 License"
 
-from flask.ext.login import UserMixin
-from flask.ext.principal import Identity
+from flask_login import UserMixin
+from flask_principal import Identity
 from werkzeug.local import LocalProxy
 import hashlib
 import os

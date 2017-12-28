--- src/octoprint/users.py.orig	2017-12-12 11:42:40 UTC
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
@@ -434,8 +434,8 @@ class User(UserMixin):
 		return {
 			"name": self._username,
 			"active": self.is_active(),
-			"admin": self.is_admin(),
-			"user": self.is_user(),
+			"admin": self.is_admin,
+			"user": self.is_user,
 			"apikey": self._apikey,
 			"settings": self._settings
 		}
@@ -449,12 +449,15 @@ class User(UserMixin):
 	def get_name(self):
 		return self._username
 
+        @property
 	def is_active(self):
 		return self._active
 
+        @property
 	def is_user(self):
 		return "user" in self._roles
 
+        @property
 	def is_admin(self):
 		return "admin" in self._roles
 
@@ -505,7 +508,7 @@ class User(UserMixin):
 		return True
 
 	def __repr__(self):
-		return "User(id=%s,name=%s,active=%r,user=%r,admin=%r)" % (self.get_id(), self.get_name(), self.is_active(), self.is_user(), self.is_admin())
+		return "User(id=%s,name=%s,active=%r,user=%r,admin=%r)" % (self.get_id(), self.get_name(), self.is_active(), self.is_user, self.is_admin)
 
 class SessionUser(wrapt.ObjectProxy):
 	def __init__(self, user):

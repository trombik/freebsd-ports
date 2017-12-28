--- setup.py.orig	2017-12-12 11:42:40 UTC
+++ setup.py
@@ -14,45 +14,45 @@ import octoprint_setuptools
 
 # Requirements for our application
 INSTALL_REQUIRES = [
-	"flask>=0.9,<0.11",
-	"Jinja2>=2.8,<2.9", # Jinja 2.9 has breaking changes WRT template scope - we can't
+	"flask>=0.9",
+	"Jinja2>=2.8",      # Jinja 2.9 has breaking changes WRT template scope - we can't
 	                    # guarantee backwards compatibility for plugins and such with that
 	                    # version, hence we need to pin to a lower version for now. See #1697
-	"werkzeug>=0.8.3,<0.9",
-	"tornado==4.0.2", # pinned for now, we need to migrate to a newer tornado, but due
+	"werkzeug>=0.8.3",
+	"tornado>=4.5.2", # pinned for now, we need to migrate to a newer tornado, but due
 	                  # to some voodoo needed to get large streamed uploads and downloads
 	                  # to work that is probably not completely straightforward and therefore
 	                  # something for post-1.3.0-stable release
 	"sockjs-tornado>=1.0.3,<1.1",
-	"PyYAML>=3.10,<3.11",
-	"Flask-Login>=0.2.2,<0.3",
-	"Flask-Principal>=0.3.5,<0.4",
-	"Flask-Babel>=0.9,<0.10",
-	"Flask-Assets>=0.10,<0.11",
+	"PyYAML>=3.10",
+	"Flask-Login>=0.2.2",
+	"Flask-Principal>=0.3.5",
+	"Flask-Babel>=0.9",
+	"Flask-Assets>=0.10",
 	"markdown>=2.6.4,<2.7",
-	"pyserial>=2.7,<2.8",
+	"pyserial>=2.7",
 	"netaddr>=0.7.17,<0.8",
 	"watchdog>=0.8.3,<0.9",
 	"sarge>=0.1.4,<0.2",
 	"netifaces>=0.10,<0.11",
 	"pylru>=1.0.9,<1.1",
-	"rsa>=3.2,<3.3",
-	"pkginfo>=1.2.1,<1.3",
-	"requests>=2.18.4,<3",
-	"semantic_version>=2.4.2,<2.5",
+	"rsa>=3.2",
+	"pkginfo>=1.2.1",
+	"requests>=2.18.1,<3",
+	"semantic_version>=2.4.2",
 	"psutil>=5.4.1,<6",
-	"Click>=6.2,<6.3",
+	"Click>=6.2",
 	"awesome-slugify>=1.6.5,<1.7",
 	"feedparser>=5.2.1,<5.3",
 	"chainmap>=1.0.2,<1.1",
-	"future>=0.15,<0.16",
-	"scandir>=1.3,<1.4",
-	"websocket-client>=0.40,<0.41",
+	"future>=0.15",
+	"scandir>=1.3",
+	"websocket-client>=0.40",
 	"python-dateutil>=2.6,<2.7",
 	"wrapt>=1.10.10,<1.11",
 	"futures>=3.1.1,<3.2",
 	"emoji>=0.4.5,<0.5",
-	"monotonic>=1.3,<1.4"
+	"monotonic>=1.3"
 ]
 
 if sys.platform == "darwin":

--- cura_app.py.orig	2019-05-02 12:06:50 UTC
+++ cura_app.py
@@ -23,7 +23,7 @@ if not known_args["debug"]:
     def get_cura_dir_path():
         if Platform.isWindows():
             return os.path.expanduser("~/AppData/Roaming/cura")
-        elif Platform.isLinux():
+        elif Platform.isUnix():
             return os.path.expanduser("~/.local/share/cura")
         elif Platform.isOSX():
             return os.path.expanduser("~/Library/Logs/cura")
@@ -36,7 +36,7 @@ if not known_args["debug"]:
 
 
 # WORKAROUND: GITHUB-88 GITHUB-385 GITHUB-612
-if Platform.isLinux(): # Needed for platform.linux_distribution, which is not available on Windows and OSX
+if Platform.isUnix(): # Needed for platform.linux_distribution, which is not available on Windows and OSX
     # For Ubuntu: https://bugs.launchpad.net/ubuntu/+source/python-qt4/+bug/941826
     # The workaround is only needed on Ubuntu+NVidia drivers. Other drivers are not affected, but fine with this fix.
     try:

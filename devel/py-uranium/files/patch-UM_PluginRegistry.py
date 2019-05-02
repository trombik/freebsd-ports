--- UM/PluginRegistry.py.orig	2019-05-02 11:57:01 UTC
+++ UM/PluginRegistry.py
@@ -716,7 +716,7 @@ class PluginRegistry(QObject):
         file_types = []
         all_types = []
 
-        if Platform.isLinux():
+        if Platform.isUnix():
             for ext, desc in self._supported_file_types.items():
                 file_types.append("{0} (*.{1} *.{2})".format(desc, ext.lower(), ext.upper()))
                 all_types.append("*.{0} *.{1}".format(ext.lower(), ext.upper()))

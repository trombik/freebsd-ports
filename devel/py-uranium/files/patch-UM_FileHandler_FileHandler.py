--- UM/FileHandler/FileHandler.py.orig	2019-03-18 10:51:44 UTC
+++ UM/FileHandler/FileHandler.py
@@ -43,7 +43,7 @@ class FileHandler(QObject):
         file_types = []
         all_types = []
 
-        if Platform.isLinux():
+        if Platform.isUnix():
             for ext, desc in self.getSupportedFileTypesRead().items():
                 file_types.append("{0} (*.{1} *.{2})".format(desc, ext.lower(), ext.upper()))
                 all_types.append("*.{0} *.{1}".format(ext.lower(), ext.upper()))

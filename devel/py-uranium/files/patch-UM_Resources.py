--- UM/Resources.py.orig	2019-05-02 11:57:30 UTC
+++ UM/Resources.py
@@ -343,7 +343,7 @@ class Resources:
                 config_path = "."
         elif Platform.isOSX():
             config_path = os.path.expanduser("~/Library/Application Support")
-        elif Platform.isLinux():
+        elif Platform.isUnix():
             try:
                 config_path = os.environ["XDG_CONFIG_HOME"]
             except KeyError:
@@ -373,7 +373,7 @@ class Resources:
         data_root_list = []
 
         # Returns all possible root paths for storing app configurations (in old and new versions)
-        if Platform.isLinux():
+        if Platform.isUnix():
             # We can cast here to str since the _getDataStorageRootPath always returns a string if platform is Linux
             data_root_list.append(os.path.join(cast(str, Resources._getDataStorageRootPath()), cls.ApplicationIdentifier))
         else:
@@ -386,7 +386,7 @@ class Resources:
     def _getDataStorageRootPath(cls) -> Optional[str]:
         # Returns the path where we store different versions of app data
         data_path = None
-        if Platform.isLinux():
+        if Platform.isUnix():
             try:
                 data_path = os.environ["XDG_DATA_HOME"]
             except KeyError:
@@ -401,7 +401,7 @@ class Resources:
             cache_path = os.getenv("LOCALAPPDATA")
         elif Platform.isOSX():
             cache_path = None
-        elif Platform.isLinux():
+        elif Platform.isUnix():
             try:
                 cache_path = os.environ["XDG_CACHE_HOME"]
             except KeyError:

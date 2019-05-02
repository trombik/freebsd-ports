--- UM/Platform.py.orig	2018-07-02 15:06:14 UTC
+++ UM/Platform.py
@@ -2,8 +2,8 @@
 # Cura is released under the terms of the LGPLv3 or higher.
 
 import sys
+import re
 
-
 ##  Convenience class to simplify OS checking and similar platform-specific handling.
 class Platform:
     class PlatformType:
@@ -11,6 +11,7 @@ class Platform:
         Linux = 2
         OSX = 3
         Other = 4
+        FreeBSD = 5
 
     ##  Check to see if we are currently running on OSX.
     @classmethod
@@ -27,6 +28,16 @@ class Platform:
     def isLinux(cls) -> bool:
         return cls.__platform_type == cls.PlatformType.Linux
 
+    ##  Check to see if we are currently running on FreeBSD.
+    @classmethod
+    def isFreeBSD(cls) -> bool:
+        return cls.__platform_type == cls.PlatformType.FreeBSD
+
+    ##  Check to see if we are currently running on Un*x.
+    @classmethod
+    def isUnix(cls) -> bool:
+        return cls.__platform_type == cls.PlatformType.Linux or cls.__platform_type == cls.PlatformType.FreeBSD
+
     ##  Get the platform type.
     @classmethod
     def getType(cls) -> int:
@@ -39,3 +50,5 @@ class Platform:
         __platform_type = PlatformType.Linux
     elif sys.platform == "darwin":
         __platform_type = PlatformType.OSX
+    elif re.match('freebsd', sys.platform):
+        __platform_type = PlatformType.FreeBSD

--- cura/Settings/GlobalStack.py.orig	2019-05-02 12:05:47 UTC
+++ cura/Settings/GlobalStack.py
@@ -254,7 +254,7 @@ class GlobalStack(CuraContainerStack):
         machine_has_heated_bed = self.getProperty("machine_heated_bed", "value")
 
         baudrate = 250000
-        if Platform.isLinux():
+        if Platform.isUnix():
             # Linux prefers a baudrate of 115200 here because older versions of
             # pySerial did not support a baudrate of 250000
             baudrate = 115200

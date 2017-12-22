--- cmake/FindSIP.py.orig	2017-12-08 01:22:57 UTC
+++ cmake/FindSIP.py
@@ -19,7 +19,7 @@ try:
     sip_version = sipcfg.sip_version
     sip_version = sipcfg.sip_version
     sip_version_str = sipcfg.sip_version_str
-    sip_bin = sipcfg.sip_bin
+    sip_bin = sipcfg.sip_bin + '-%%PYTHON_VER%%'
     default_sip_dir = sipcfg.default_sip_dir
     sip_inc_dir = sipcfg.sip_inc_dir
 

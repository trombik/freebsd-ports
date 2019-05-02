--- plugins/CuraEngineBackend/CuraEngineBackend.py.orig	2019-05-02 12:08:00 UTC
+++ plugins/CuraEngineBackend/CuraEngineBackend.py
@@ -62,7 +62,7 @@ class CuraEngineBackend(QObject, Backend):
             default_engine_location = os.path.join(CuraApplication.getInstallPrefix(), "bin", executable_name)
         if hasattr(sys, "frozen"):
             default_engine_location = os.path.join(os.path.dirname(os.path.abspath(sys.executable)), executable_name)
-        if Platform.isLinux() and not default_engine_location:
+        if Platform.isUnix() and not default_engine_location:
             if not os.getenv("PATH"):
                 raise OSError("There is something wrong with your Linux installation.")
             for pathdir in cast(str, os.getenv("PATH")).split(os.pathsep):

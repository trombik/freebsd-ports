--- cura/Backups/Backup.py.orig	2019-05-02 12:03:48 UTC
+++ cura/Backups/Backup.py
@@ -46,7 +46,7 @@ class Backup:
 
         # We copy the preferences file to the user data directory in Linux as it's in a different location there.
         # When restoring a backup on Linux, we move it back.
-        if Platform.isLinux(): #TODO: This should check for the config directory not being the same as the data directory, rather than hard-coding that to Linux systems.
+        if Platform.isUnix(): #TODO: This should check for the config directory not being the same as the data directory, rather than hard-coding that to Linux systems.
             preferences_file_name = self._application.getApplicationName()
             preferences_file = Resources.getPath(Resources.Preferences, "{}.cfg".format(preferences_file_name))
             backup_preferences_file = os.path.join(version_data_dir, "{}.cfg".format(preferences_file_name))
@@ -129,7 +129,7 @@ class Backup:
         extracted = self._extractArchive(archive, version_data_dir)
 
         # Under Linux, preferences are stored elsewhere, so we copy the file to there.
-        if Platform.isLinux():
+        if Platform.isUnix():
             preferences_file_name = self._application.getApplicationName()
             preferences_file = Resources.getPath(Resources.Preferences, "{}.cfg".format(preferences_file_name))
             backup_preferences_file = os.path.join(version_data_dir, "{}.cfg".format(preferences_file_name))

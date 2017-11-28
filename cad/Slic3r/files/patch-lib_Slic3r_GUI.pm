--- lib/Slic3r/GUI.pm.orig	2018-05-08 22:47:09 UTC
+++ lib/Slic3r/GUI.pm
@@ -442,7 +442,7 @@ sub scan_serial_ports {
         }
     } else {
         # UNIX and OS X
-        push @ports, glob '/dev/{ttyUSB,ttyACM,tty.,cu.,rfcomm}*';
+        push @ports, glob '/dev/{ttyUSB,ttyACM,tty.,cu.,rfcomm,ttyU}*';
     }
     
     return grep !/Bluetooth|FireFly/, @ports;

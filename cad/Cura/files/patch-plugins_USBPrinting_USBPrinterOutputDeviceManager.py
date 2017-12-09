--- plugins/USBPrinting/USBPrinterOutputDeviceManager.py.orig	2017-10-17 14:44:27 UTC
+++ plugins/USBPrinting/USBPrinterOutputDeviceManager.py
@@ -83,7 +83,10 @@ class USBPrinterOutputDeviceManager(QObject, OutputDev
 
     def _updateThread(self):
         while self._check_updates:
-            result = self.getSerialPortList(only_list_usb = True)
+            if platform.system() == "FreeBSD":
+                result = self.getSerialPortList(only_list_usb = False)
+            else:
+                result = self.getSerialPortList(only_list_usb = True)
             self._addRemovePorts(result)
             time.sleep(5)
 
@@ -162,6 +165,8 @@ class USBPrinterOutputDeviceManager(QObject, OutputDev
 
         if platform.system() == "Linux":
             baudrate = 115200
+        elif platform.system() == "FreeBSD":
+            baudrate = 115200
         else:
             baudrate = 250000
 

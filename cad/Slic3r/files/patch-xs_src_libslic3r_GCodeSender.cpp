--- xs/src/libslic3r/GCodeSender.cpp.orig	2018-05-08 22:47:09 UTC
+++ xs/src/libslic3r/GCodeSender.cpp
@@ -8,7 +8,7 @@
 #include <boost/date_time/posix_time/posix_time.hpp>
 #include <boost/lexical_cast.hpp>
 
-#if defined(__APPLE__) || defined(__OpenBSD__)
+#if defined(__APPLE__) || defined(__OpenBSD__) || defined(__FreeBSD__)
 #include <termios.h>
 #endif
 #ifdef __APPLE__
@@ -140,7 +140,7 @@ GCodeSender::set_baud_rate(unsigned int baud_rate)
         if (ioctl(handle, TCSETS2, &ios))
             printf("Error in TCSETS2: %s\n", strerror(errno));
 		
-#elif __OpenBSD__
+#elif __OpenBSD__ || __FreeBSD__
 		struct termios ios;
 		::tcgetattr(handle, &ios);
 		::cfsetspeed(&ios, baud_rate);

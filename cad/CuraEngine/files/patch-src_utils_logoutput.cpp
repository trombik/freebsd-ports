--- src/utils/logoutput.cpp.orig	2019-05-02 04:58:51 UTC
+++ src/utils/logoutput.cpp
@@ -24,10 +24,10 @@ void enableProgressLogging()
 
 void logError(const char* fmt, ...)
 {
+    va_list args;
+    va_start(args, fmt);
     #pragma omp critical
     {
-        va_list args;
-        va_start(args, fmt);
         fprintf(stderr, "[ERROR] ");
         vfprintf(stderr, fmt, args);
         va_end(args);
@@ -37,10 +37,10 @@ void logError(const char* fmt, ...)
 
 void logWarning(const char* fmt, ...)
 {
+    va_list args;
+    va_start(args, fmt);
     #pragma omp critical
     {
-        va_list args;
-        va_start(args, fmt);
         fprintf(stderr, "[WARNING] ");
         vfprintf(stderr, fmt, args);
         va_end(args);
@@ -50,10 +50,10 @@ void logWarning(const char* fmt, ...)
 
 void logAlways(const char* fmt, ...)
 {
+    va_list args;
+    va_start(args, fmt);
     #pragma omp critical
     {
-        va_list args;
-        va_start(args, fmt);
         vfprintf(stderr, fmt, args);
         va_end(args);
         fflush(stderr);
@@ -65,10 +65,10 @@ void log(const char* fmt, ...)
     if (verbose_level < 1)
         return;
 
+    va_list args;
+    va_start(args, fmt);
     #pragma omp critical
     {
-        va_list args;
-        va_start(args, fmt);
         vfprintf(stderr, fmt, args);
         va_end(args);
         fflush(stderr);
@@ -81,10 +81,10 @@ void logDebug(const char* fmt, ...)
     {
         return;
     }
+    va_list args;
+    va_start(args, fmt);
     #pragma omp critical
     {
-        va_list args;
-        va_start(args, fmt);
         fprintf(stderr, "[DEBUG] ");
         vfprintf(stderr, fmt, args);
         va_end(args);

--- src/share/poudriere/ports.sh.orig	2018-03-28 16:43:06 UTC
+++ src/share/poudriere/ports.sh
@@ -395,4 +395,5 @@ if [ ${UPDATE} -eq 1 ]; then
 	esac
 
 	pset ${PTNAME} timestamp $(clock -epoch)
+	run_hook ports_update "done"
 fi

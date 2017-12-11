--- resources/shaders/grid.shader.orig	2017-12-09 08:25:18 UTC
+++ resources/shaders/grid.shader
@@ -31,10 +31,10 @@ fragment =
         vec4 minorGridColor = mix(u_plateColor, u_gridColor1, 1.0 - min(minorLine, 1.0));
 
         // Compute anti-aliased world-space major grid lines
-        vec2 majorGrid = abs(fract(coord / 10 - 0.5) - 0.5) / fwidth(coord / 10);
+        vec2 majorGrid = abs(fract(coord / 10.0 - 0.5) - 0.5) / fwidth(coord / 10.0);
         float majorLine = min(majorGrid.x, majorGrid.y);
 
-        frag_color = mix(minorGridColor, u_gridColor0, 1.0 - min(majorLine, 1.0));
+        gl_FragColor = mix(minorGridColor, u_gridColor0, 1.0 - min(majorLine, 1.0));
     }
 
 vertex41core =
@@ -72,7 +72,7 @@ fragment41core =
         vec4 minorGridColor = mix(u_plateColor, u_gridColor1, 1.0 - min(minorLine, 1.0));
 
         // Compute anti-aliased world-space major grid lines
-        vec2 majorGrid = abs(fract(coord / 10 - 0.5) - 0.5) / fwidth(coord / 10);
+        vec2 majorGrid = abs(fract(coord / 10.0 - 0.5) - 0.5) / fwidth(coord / 10.0);
         float majorLine = min(majorGrid.x, majorGrid.y);
 
         frag_color = mix(minorGridColor, u_gridColor0, 1.0 - min(majorLine, 1.0));

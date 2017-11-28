--- lib/Slic3r.pm.orig	2018-04-07 08:21:03 UTC
+++ lib/Slic3r.pm
@@ -42,7 +42,7 @@ warn "Running Slic3r under Perl 5.16 is neither suppor
 
 use FindBin;
 # Path to the images.
-my $varpath = decode_path($FindBin::Bin) . "/var";
+my $varpath = "%%DATADIR%%";
 if ($^O eq 'darwin' && !-d $varpath) {
     $varpath = decode_path($FindBin::Bin) . "/../Resources/var";
 }

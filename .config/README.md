# `.config` directory

This directory contains per-tree configurations.

## `packages.txt`

The file contains a list of package origins to build. The file is passed to
`poudriere(8)` with `-f ${filename}` when building packages. See
`poudriere(8)`.

## `Makefile`

`Makefile` in the top directory installs the configurations, such as per-jail,
per-build `options`.

## `update_master.sh`

The files forcibly updates, and _discards local modification_, in the `master`
branch from the upstream. Local modifications must NOT committed to the
`master` branch.
